from odoo import models, fields


class MasterBank(models.Model):
    _name = 'master.bank'
    _description = 'Module for manage bank'

    name = fields.Char()