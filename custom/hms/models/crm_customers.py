from odoo import api, models, fields
from odoo.exceptions import UserError


class CrmCustomersInherit(models.Model):
    _inherit = 'res.partner'

    salary = fields.Float()

    vat = fields.Char(compute="calc_tax", store=True, required=True)

    related_patient_id = fields.Many2one("hms.patient")

    @api.depends('salary')
    def calc_tax(self):
        for record in self:
            record.vat = record.salary * 0.2

    def unlink(self):
        for record in self:
            if record.related_patient_id:
                raise UserError("Can't delete customer,this customer have patient")
        super().unlink()

    # @api.constrains("email")
    # def check_email(self):
    #     for record in self:
    #         if record.email == record.related_patient_id.email:
    #             raise UserError('This email used by patient')
    #     customers = self.search([('email', '=', self.email)])
    #     if len(customers) > 1:
    #         raise UserError('Email already existed')
    #     return True

    @api.constrains("related_patient_id")
    def check_valid_email(self):
        for record in self:
            if record.related_patient_id.email != record.email:
                if self.env['hms.patient'].search([('email', '=', record.email)]):
                    raise UserError("Email already existed")

