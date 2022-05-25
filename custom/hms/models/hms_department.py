from odoo import models, fields, api


class Department(models.Model):
    _name = "hms.department"
    name = fields.Text()
    capacity = fields.Integer(default=0)
    is_opened = fields.Boolean()
    patient_ids = fields.One2many(comodel_name='hms.patient', inverse_name='id', string="Patients")
