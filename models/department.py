from odoo import models, fields


class Department(models.Model):
    _name = 'department'
    _description = 'department'

    name = fields.Char(string='Department')
    hod_id = fields.Many2one('res.partner', string='HOD')
