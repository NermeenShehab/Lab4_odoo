from odoo import models, fields


class Doctor(models.Model):
    _name = "hms.doctor"
    _rec_name = "first_name"
    first_name = fields.Text()
    last_name = fields.Text()
    image = fields.Image()
    patients = fields.Many2many(comodel_name='hms.patient', read_only=True)