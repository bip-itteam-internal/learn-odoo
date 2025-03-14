from odoo import api, fields, models, _

class ProjectDepartment(models.Model):
    _name = 'project.department'
    _description = 'Project Department'
    
    name = fields.Char(string='Department Name', required=True)
    code = fields.Char(string='Code', required=True)
    manager_id = fields.Many2one('res.users', string='Manager')
    description = fields.Text(string='Description')
    member_ids = fields.One2many('project.department.member', 'department_id', string='Members')
    task_ids = fields.One2many('project.task', 'department_id', string='Tasks')
    project_ids = fields.Many2many('project.project', string='Projects', compute='_compute_projects')
    active = fields.Boolean(default=True)
    
    # Statistics fields
    total_members = fields.Integer(string='Total Members', compute='_compute_stats')
    total_tasks = fields.Integer(string='Total Tasks', compute='_compute_stats')
    completed_tasks = fields.Integer(string='Completed Tasks', compute='_compute_stats')
    
    @api.depends('task_ids.project_id')
    def _compute_projects(self):
        for dept in self:
            dept.project_ids = dept.task_ids.mapped('project_id')
    
    @api.depends('member_ids', 'task_ids', 'task_ids.stage_id')
    def _compute_stats(self):
        for dept in self:
            dept.total_members = len(dept.member_ids)
            all_tasks = dept.task_ids
            dept.total_tasks = len(all_tasks)
            dept.completed_tasks = len(all_tasks.filtered(lambda t: t.stage_id.is_closed))
    
    def action_view_tasks(self):
        """View all tasks for this department"""
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("project.action_view_task")
        action['domain'] = [('department_id', '=', self.id)]
        action['context'] = {'default_department_id': self.id}
        return action