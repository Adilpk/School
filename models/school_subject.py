# -*- coding: utf-8 -*-
from odoo import models, fields


class SchoolSubject(models.Model):
    """ create a subject module to store subject and department"""
    _name = 'school.subject'
    _description = 'Subject'

    name = fields.Char(string='Subject')
    department_id = fields.Many2one('department', string='Department')
