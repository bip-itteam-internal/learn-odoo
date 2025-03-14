from odoo import api, fields, models, _
from datetime import datetime, timedelta
import json

class TaskAnalysisWizard(models.TransientModel):
    _name = 'task.analysis.wizard'
    _description = 'Task Analysis Wizard'
    
    project_id = fields.Many2one('project.project', string='Project', required=True)
    department_id = fields.Many2one('project.department', string='Department',
                                    domain="[('id', 'in', department_ids)]")
    department_ids = fields.Many2many('project.department', string='Available Departments',
                                     compute='_compute_department_ids')
    date_from = fields.Date(string='From Date')
    date_to = fields.Date(string='To Date', default=fields.Date.today)
    include_bottlenecks = fields.Boolean(string='Highlight Bottlenecks', default=True)
    
    analysis_result = fields.Text(string='Analysis Result', readonly=True)
    chart_data = fields.Text(string='Chart Data', readonly=True)
    
    @api.depends('project_id')
    def _compute_department_ids(self):
        for wizard in self:
            wizard.department_ids = wizard.project_id.department_ids
    
    def action_analyze(self):
        self.ensure_one()
        
        # Build domain for task search
        domain = [('project_id', '=', self.project_id.id)]
        if self.department_id:
            domain.append(('department_id', '=', self.department_id.id))
        if self.date_from:
            domain.append(('create_date', '>=', self.date_from))
        if self.date_to:
            domain.append(('create_date', '<=', self.date_to))
        
        tasks = self.env['project.task'].search(domain)
        
        # Generate analytics
        total_tasks = len(tasks)
        completed_tasks = len(tasks.filtered(lambda t: t.stage_id.is_closed))
        overdue_tasks = len(tasks.filtered(lambda t: t.date_deadline and t.date_deadline < fields.Date.today() and not t.stage_id.is_closed))
        
        bottleneck_tasks = tasks.filtered(lambda t: t.is_bottleneck)
        bottlenecks_count = len(bottleneck_tasks)
        
        # Department performance analysis
        dept_data = {}
        
        for task in tasks:
            dept = task.department_id
            if not dept:
                continue
                
            if dept not in dept_data:
                dept_data[dept] = {
                    'total': 0,
                    'completed': 0,
                    'overdue': 0,
                    'bottlenecks': 0,
                    'avg_delay': 0,
                    'total_delay': 0
                }
            
            dept_data[dept]['total'] += 1
            
            if task.stage_id.is_closed:
                dept_data[dept]['completed'] += 1
                
            if task.date_deadline and task.date_deadline < fields.Date.today() and not task.stage_id.is_closed:
                dept_data[dept]['overdue'] += 1
                delay = (fields.Date.today() - task.date_deadline).days
                dept_data[dept]['total_delay'] += delay
                
            if task.is_bottleneck:
                dept_data[dept]['bottlenecks'] += 1
        
        # Calculate average delays
        for dept in dept_data:
            if dept_data[dept]['overdue'] > 0:
                dept_data[dept]['avg_delay'] = dept_data[dept]['total_delay'] / dept_data[dept]['overdue']
        
        # Format results
        result = {
            'summary': {
                'total_tasks': total_tasks,
                'completed_tasks': completed_tasks,
                'completion_rate': (completed_tasks / total_tasks * 100) if total_tasks else 0,
                'overdue_tasks': overdue_tasks,
                'bottlenecks_count': bottlenecks_count,
            },
            'departments': []
        }
        
        for dept, data in dept_data.items():
            result['departments'].append({
                'id': dept.id,
                'name': dept.name,
                'total': data['total'],
                'completed': data['completed'],
                'completion_rate': (data['completed'] / data['total'] * 100) if data['total'] else 0,
                'overdue': data['overdue'],
                'bottlenecks': data['bottlenecks'],
                'avg_delay': round(data['avg_delay'], 1)
            })
        
        # Store results
        self.analysis_result = json.dumps(result)
        
                # Generate chart data
        chart_data = {
            'labels': [dept['name'] for dept in result['departments']],
            'datasets': [
                {
                    'label': 'Completion Rate (%)',
                    'data': [dept['completion_rate'] for dept in result['departments']],
                    'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                    'borderColor': 'rgba(75, 192, 192, 1)',
                },
                {
                    'label': 'Bottlenecks',
                    'data': [dept['bottlenecks'] for dept in result['departments']],
                    'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                    'borderColor': 'rgba(255, 99, 132, 1)',
                }
            ]
        }
        
        self.chart_data = json.dumps(chart_data)
        
        return {
            'name': 'Task Analysis Results',
            'type': 'ir.actions.act_window',
            'res_model': 'task.analysis.wizard',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
            'context': {'form_view_initial_mode': 'edit'},
            'views': [(False, 'form')],
        }