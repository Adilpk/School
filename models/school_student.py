# -*- coding:utf-8 -*-
from datetime import date

from odoo import api, fields, models


class SchoolStudent(models.Model):
    """ create a new model named school student for registration purpose"""
    _name = 'school.student'
    _description = 'student'
    _rec_name = 'registration_number'
    _sql_constraints = [('aadhar_number_unique', 'UNIQUE(aadhar_number)', 'this Aadhar Number is already used')]

    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    father = fields.Char(string='Father')
    mother = fields.Char(string='Mother')
    school_ids = fields.Many2many('res.company', default=lambda self: self.env.company)
    communication_address = fields.Text(string='Communication Address')
    same_as = fields.Boolean(string='Same As Communication Address')
    permanent_address = fields.Text(string='Permanent Address')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    dob = fields.Date(string='Date of Birth')
    age = fields.Char(string='Age', compute='_compute_age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    registration_date = fields.Date(string='Registration Date', default=fields.Date.context_today)
    photo = fields.Image(string='Photo')
    department_id = fields.Many2one('school.department', string='Previous Department')
    class_id = fields.Many2one('school.class', string='Previous Class', domain="[('department_id', '=',"
                                                                               " department_id)]")
    tc = fields.Binary(string='Tc')
    aadhar_number = fields.Char(string='Aadhar Number', readonly=True)
    registration_number = fields.Char(string='Registration Number', readonly=True, copy=False, default=lambda self: self
                                      .env['ir.sequence'].next_by_code('school.student.sequence'))
    admission_number = fields.Char(string='Admission Number')
    status = fields.Selection([('draft', 'Draft'), ('registered', 'Registered')],
                              string='status', default='draft')

    def button_register(self):
        if self.status == 'draft':
            self.admission_number = self.env['ir.sequence'].next_by_code('registered.student.sequence')
            self.status = 'registered'

    @api.depends('dob')
    def _compute_age(self):
        today = date.today()
        if today > self.dob:
            for rec in self:
                if rec.dob:
                    date_of_birth = fields.Date.from_string(rec.dob)
                    rec.age = date.today().year - date_of_birth.year
        else:
            self.age = 0