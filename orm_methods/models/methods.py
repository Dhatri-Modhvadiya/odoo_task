from odoo import models, fields, api

class Methods(models.Model):
    # Attributes
    _name = "methods.info"
    _description = "Method"

    # fields
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    manager = fields.Text(string="Manager")
    employee_ids = fields.Integer(string="Employees")
