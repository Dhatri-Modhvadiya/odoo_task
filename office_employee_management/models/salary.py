from odoo import models, fields

class Salary(models.Model):
    _name = 'salary.info'
    _description = 'Employee salary'


    salary_amount = fields.Integer(string="Salary amount")
    employee_id = fields.Integer(string='Employee_Id', index=True)



