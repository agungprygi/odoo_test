# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = "Patient Records"
    
    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', required=True, tracking=True)
    is_child = fields.Boolean(string='Is a Child?', tracking=True)
    notes = fields.Text(string='Notes')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender', tracking=True)
    capitalize_name = fields.Char(string='Capitalize Name', compute='_compute_capitalize_name', store=True)
    
    @api.constrains('is_child', 'age')
    def _check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(_('Age has to be recorded for child patients.'))
    
    @api.depends('name')
    def _compute_capitalize_name(self):
        for rec in self:
            if rec.name:
                rec.capitalize_name = rec.name.upper()
            else:
                rec.capitalize_name = ''
    
    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False