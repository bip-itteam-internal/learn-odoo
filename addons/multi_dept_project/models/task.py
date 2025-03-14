from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class ProjectTask(models.Model):
    _inherit = 'project.task'
    
    department_id = fields.Many2one('project.department', string='Responsible Department')
    responsible_id = fields.Many2one('project.department.member', string='Responsible Member',
                                      domain="[('department_id', '=', department_id)]")
    date_start = fields.Datetime(string='Start Date')
    date_end = fields.Datetime(string='End Date')
    
    # Dependencies
    dependency_ids = fields.Many2many('project.task', 'project_task_dependency_rel',
                                      'task_id', 'depends_on_id', string='Dependencies')
    dependent_task_ids = fields.Many2many('project.task', 'project_task_dependency_rel',
                                          'depends_on_id', 'task_id', string='Dependent Tasks')
    
    @api.constrains('responsible_id', 'department_id')
    def _check_responsible_department(self):
        for task in self:
            if task.responsible_id and task.department_id and task.responsible_id.department_id != task.department_id:
                raise ValidationError(_("Responsible member must belong to the assigned department."))