from odoo import models, fields, api
from datetime import datetime

class CustomNotes(models.Model):
    _name = 'custom.notes'
    _description = 'Custom Notes'
    
    name = fields.Char(string='Title', required=True)
    date = fields.Date(string='Date', default=fields.Date.today)
    content = fields.Text(string='Content')