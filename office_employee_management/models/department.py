from odoo import models, fields, api

class Department(models.Model):
    # Attributes
    _name = "department.info"
    _description = "Department"

    # fields
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    manager = fields.Many2one('employee.info', string="Manager")
    employee_ids = fields.Many2many('employee.info', string="Employees")

