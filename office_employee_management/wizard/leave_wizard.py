from odoo import models, fields, api,_

class leaveReportWizard(models.TransientModel):
   _name = 'leave_wizard'

   employee_id = fields.Many2one('employee.info', string='Employee', required=True)
   start_date = fields.Date(string='Start Date', required=True)
   end_date = fields.Date(string='End Date', required=True)
   reason = fields.Text(string='Reason', required=True)

