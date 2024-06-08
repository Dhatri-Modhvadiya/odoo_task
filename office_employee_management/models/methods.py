from odoo import models, fields, api

class Department(models.Model):
    # Attributes
    _name = "method.info"
    _description = "orm methods"

    # fields
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    manager = fields.Many2one('domain.info', string="Manager")
    employee_ids = fields.Many2many('employee.info', string="Employees")





