from odoo import api, fields, models, _

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = ['mail.thread']
    _description = "Doctor Records"
    _rec_name = 'ref'
    
    name = fields.Char(string='Name', required=True)
    ref = fields.Char(string='Ref', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')
    
    @api.depends('ref', 'name')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f'{rec.ref} - {rec.name}'