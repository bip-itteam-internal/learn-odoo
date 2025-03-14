from odoo import models, fields


class Assessment(models.Model):
    _name = 'assessment.assessment'
    _description = 'Assessment'
    
    name = fields.Char(string='Assessment Name', required=True)
    description = fields.Text(string='Description')
    
    # Field untuk user yang di-assign
    assigned_user_id = fields.Many2one('res.users', string='Assigned User')
    
    # Field untuk user yang membuat assessment (opsional)
    created_by = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.user.id, readonly=True)
    
    # Tanggal pembuatan assessment
    date_created = fields.Date(string='Date Created', default=fields.Date.today, readonly=True)
    
    # Status assessment
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')