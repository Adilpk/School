# -*- coding:utf-8 -*-
from odoo import models, fields


class SchoolYear(models.Model):
    """create academic year"""
    _name = 'school.year'
    _description = 'Academic Year'

    name = fields.Char(string='Year')
