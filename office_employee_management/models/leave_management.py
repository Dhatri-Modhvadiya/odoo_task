import self
from odoo import models, fields, api,_

class Leave_Management(models.Model):
    # Attributes
    _name = 'leave.info'
    _description = 'Leave Management '
    _rec_name = "employee_id"

    def check_orm(self):
        search_var = self.env['leave.info'].search([])
        print("Search for var",search_var)


    # fields
    employee_id = fields.Integer(string="Employee_Id")
    leave_type = fields.Selection([('sick leave', 'Sick Leave'), ('maternity leave', 'Maternity Leave'), ('casual leave', 'Casual Leave'), ('annual leave', 'Annual Leave'),('others','Others')],string='Leave_Type', index=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    reason = fields.Text(string='Reason', required=True)
    # emp_id field define for ir sequence
    emp_id = fields.Char(string="employee ID", readonly=True, copy=False)



    # function for defining ir sequence
    @api.model
    def create(self, vals):
        if vals.get('emp_id', ('New')) == ('New'):
            vals['emp_id'] = self.env['ir.sequence'].next_by_code('customer.sequence') or _('New')
        return super(Leave_Management, self).create(vals)

