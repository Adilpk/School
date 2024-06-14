# -*- coding: utf-8 -*-
from odoo import models, fields


class Department(models.Model):
    """create department model to store department and head of
    department"""
    _name = 'department'
    _description = 'department'

    name = fields.Char(string='Department')
    hod_id = fields.Many2one('res.partner', string='HOD')
