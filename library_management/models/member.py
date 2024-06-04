from odoo import models, fields

class MemberInformation(models.Model):
    _name = "member.info"
    _description = "this model is about member Information"

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Integer(string='Phone')
    address = fields.Text(string='Address')

class JavascriptFunction(models.Model):
    _inherit = 'sale.order'

