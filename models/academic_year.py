# -*- coding:utf-8 -*-
from odoo import models, fields


class AcademicYear(models.Model):
    """create academic year"""
    _name = 'academic.year'
    _description = 'Academic Year'

    name = fields.Char(string='Year')
