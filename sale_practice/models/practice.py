from odoo import models, fields, api, _

class PracticeInformation(models.Model):
     #Attributes
    _name = "practice.info1"
    _description = "This model is about practice"

    name = fields.Char(string='Order Reference', required=True)
    customer_id = fields.Many2one('custom_sales.customer', string='Customer')

class Customer(models.Model):
    _name = 'custom_sales.customer'
    _description = 'Customer'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    



