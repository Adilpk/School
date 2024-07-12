# -*- coding: utf-8 -*-
from odoo import fields, models


class SchoolEvents(models.Model):
    """ create a model for managing school events"""
    _name = 'school.events'
    _description = 'Event'

    name = fields.Char(string='Event', required=True)
    date_start = fields.Date(string='Start Date')
    date_end = fields.Date(string='End Date')
    location = fields.Char(string='Location')
    description = fields.Text(string='Description')
    image = fields.Binary(string='Event Image')




