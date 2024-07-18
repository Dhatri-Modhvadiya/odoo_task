from odoo import api, fields, models

class Location(models.Model):
    _name = "res.location"
    _description = "point od sale location"

    name = fields.Char(string="Name")
    address = fields.Char(string="Address")
    pin_code = fields.Char(string="Pin Code")
