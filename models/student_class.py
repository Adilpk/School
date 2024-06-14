from odoo import models, fields


class StudentClass(models.Model):
    _name = 'student.class'
    _description = 'class'

    name = fields.Char(str='Class')
    department_id = fields.Many2one('department', string='Department')
