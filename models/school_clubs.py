# -*- coding: utf-8 -*-
from odoo import fields, models


class SchoolClubs(models.Model):
    _name = 'school.clubs'
    _description = 'Club'

    name = fields.Char(string='Club', required=True)
    established_date = fields.Date(string='Established date')
    description = fields.Char(string='Description')
    student_ids = fields.Many2many('school.student', string='Student')



