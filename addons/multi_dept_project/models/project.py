from odoo import api, fields, models

class Project(models.Model):
    _inherit = 'project.project'
    
    is_multi_department = fields.Boolean(string='Multi-Department Project')
    department_ids = fields.Many2many('project.department', string='Departments')