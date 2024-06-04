import base64
import io
from datetime import datetime, timedelta

import self
import xlsxwriter
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


# birthday reminder schedular task :-
class EmailSchedular(models.Model):
    _inherit = "res.partner"
    dob =  fields.Date(string = "DOB")
    start_date = fields.Date(string = "Start_Date")

    def run_bdy_notification(self):
        today = fields.Date.today()
        today_month_day = today.strftime('%m-%d')
        all_records = self.search([])
        for rec in all_records:
            if rec.dob and rec.dob.strftime('%m-%d') == today_month_day:
                email_values = {
                    'email_to': rec.email,
                    'subject': f"Happy Birthday {rec.name}"
                }
                print(f"Happy Birthday {rec.display_name}")
                mail_template = self.env.ref('office_employee_management.birthday_email_template')
                mail_template.send_mail(rec.id, email_values=email_values, force_send=True)
                print(f"Happy Birthday {rec.display_name} Again")




class reportMonthly(models.Model):
    _inherit = "sale.order"

    def generates_customer_report(self):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        sheet = workbook.add_worksheet('customer')
        admin = self.env.user.name
        mail = self.env.user.email
        today_date = datetime.today()
        last_month_date = today_date-timedelta(days=today_date.day)

        bold_format = workbook.add_format(
            {'bold': True, 'align': 'center', 'font_size': 12, 'bg_color': '#FFA500',
             'border': True})
        normal_format = workbook.add_format({'text_wrap': True, 'align': 'center', 'font_size': 10})
        number_format = workbook.add_format({'text_wrap': True, 'align': 'right', 'font_size': 10})
        text_formate = workbook.add_format({'text_wrap': True, 'align': 'left', 'font_size': 10})
        date_format = workbook.add_format({'num_format': 'dd/mm/yy', 'align': 'center', 'font_size': 10})
        sheet.set_column('A:I', 12)  # Adjust the width as needed
        # Set row height
        sheet.set_default_row(25)  # Adjust the height as needed
        row = 1
        col = 0
        data = self.search([('user_id', '=', admin),('date_order', '>=',last_month_date),('date_order', '<=',today_date)])
        # record = self.env['sale.order'].browse(data)

        # Write headers with bold format
        sheet.write('A1', 'Number', bold_format)
        sheet.write('B1', 'Date', bold_format)
        sheet.write('C1', 'Status', bold_format)
        sheet.write('D1', 'Total', bold_format)
        sheet.write('E1', 'Name', bold_format)
        sheet.write('F1', 'Partner', bold_format)
        sheet.write('G1', 'Company', bold_format)
        # sheet.write('H1', 'Tags', bold_format)
        sheet.write('H1', 'Sale Team', bold_format)

        # row += 1
        for rec in data:
            sheet.write(row, col, rec.name or '',
                        normal_format)  # Changed rec.name to rec.name or '' to avoid NoneType error
            sheet.write(row, col + 1, rec.date_order.strftime('%Y-%m-%d') if rec.date_order else '', date_format)
            sheet.write(row, col + 2, rec.state or '', normal_format)
            sheet.write(row, col + 3, rec.amount_total or 0.0, number_format)
            sheet.write(row, col + 4, rec.user_id.name or 'NA', text_formate)
            sheet.write(row, col + 5, rec.partner_id.name or 'NA', text_formate)
            sheet.write(row, col + 6, rec.company_id.name or 'NA', text_formate)
            # sheet.write(row, col + 7, rec.tag_ids.name or 'NA', normal_format)
            sheet.write(row, col + 7, rec.team_id.name or 'NA', text_formate)

            row += 1

        workbook.close()
        output.seek(0)

        # Encode the file to base64
        excel_file = base64.b64encode(output.read())
        output.close()

        # Create an attachment
        attachment = self.env['ir.attachment'].create({
            'name': f'{self.name}_report.xlsx',  # Changed from f'{self.name}_report.xlsx'
            'type': 'binary',
            'datas': excel_file,
            'res_model': 'sale.order',
            'res_id': self.id,
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        })

        email_values = {
            'mailto:email_from':'dhatri@mail.com',
            'email_to': f'{mail}',
            'subject': f"Report from",
            'attachment_ids': [(6, 0, [attachment.id])]
        }

        # Send a single email with the report attachment to all recipients
        mail_template = self.env.ref('office_employee_management.mail_monthly_report_template')
        mail_template.send_mail(self.env.user.id, email_values=email_values, force_send=True)

        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'self',
        }






