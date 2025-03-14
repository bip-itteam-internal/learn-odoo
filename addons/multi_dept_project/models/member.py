from odoo import api, fields, models

class ProjectDepartmentMember(models.Model):
    _name = 'project.department.member'
    _description = 'Project Department Member'
    
    user_id = fields.Many2one('res.users', string='User', required=True)
    department_id = fields.Many2one('project.department', string='Department', required=True)
    role = fields.Char(string='Role in Department')
    join_date = fields.Date(string='Join Date', default=fields.Date.today)
    
    # Statistics
    assigned_tasks = fields.Integer(string='Assigned Tasks', compute='_compute_task_stats')
    completed_tasks = fields.Integer(string='Completed Tasks', compute='_compute_task_stats')
    overdue_tasks = fields.Integer(string='Overdue Tasks', compute='_compute_task_stats')
    
    @api.depends('user_id', 'department_id')
    def _compute_task_stats(self):
        for member in self:
            domain = [
                ('responsible_id', '=', member.id)
            ]
            all_tasks = self.env['project.task'].search(domain)
            member.assigned_tasks = len(all_tasks)
            member.completed_tasks = len(all_tasks.filtered(lambda t: t.stage_id.is_closed))
            today = fields.Date.today()
            member.overdue_tasks = len(all_tasks.filtered(
                lambda t: t.date_deadline and t.date_deadline < today and not t.stage_id.is_closed
            ))