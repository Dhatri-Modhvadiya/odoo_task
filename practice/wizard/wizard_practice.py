from odoo import models,fields


class PracticeOdooWizard(models.TransientModel):
    _name = 'model.info.wizard'
    _description = ' Wizard which will update the informaation '

    name = fields.Char(string="Name")
    dob = fields.Date(string="DOB")
    country = fields.Many2one('res.country', string="country")
    country_ids = fields.Many2many('res.country', string="country_id")
    country_code = fields.Char(string="country_code", related="country.code")
    mobile = fields.Char(string="Mobile", default="1234567890")
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', "Male"), ('female', 'Female')], string="gender")
    hand_salary = fields.Float(string="In Hand Salary")
    epf_esi = fields.Float(string="EPF+ESI")
    ctc_salary = fields.Float(string="CTC")


def update_info_fun(self):
    active_id = self.context.get('active_id')
    print('active-id----',active_id)

