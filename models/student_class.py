# -*- coding: utf-8 -*-
from odoo import models, fields


class StudentClass(models.Model):
    """ create a class model to store class and department"""
    _name = 'student.class'
    _description = 'class'

    name = fields.Char(str='Class')
    department_id = fields.Many2one('department', string='Department')
