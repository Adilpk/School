# -*- coding: utf-8 -*-
from odoo import models, fields


class SchoolClass(models.Model):
    """ create a class model to store class and department"""
    _name = 'school.class'
    _description = 'class'

    name = fields.Char(str='Class')
    department_id = fields.Many2one('school.department', string='Department')
    hod_id = fields.Many2one(related='department_id.hod_id',string='HOD',strore=True)
    school_id = fields.Many2one('res.company',
                                string='Current School')
