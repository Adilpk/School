# -*- coding: utf-8 -*-
from odoo import models, fields


class SchoolDepartment(models.Model):
    """create department model to store department and head of
    department"""
    _name = 'school.department'
    _description = 'Department'

    name = fields.Char(string='Department')
    hod_id = fields.Many2one('res.partner', string='Head of Department')
