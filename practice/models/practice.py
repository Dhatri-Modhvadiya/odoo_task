import io

import xlsxwriter
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import xlwt
import base64
from io import BytesIO

from odoo17.odoo import exceptions


# print(">>>>>>>>>>>>>>>>>>>>>>>>>>hello")
# filename = self.name
# workbook = xlwt.Workbook(encoding='utf-8')
# sheet1 = workbook.add_sheet('Staff', cell_overwrite_ok=True)
# format1 = xlwt.easyxf(
#     'align :horiz center; font :color  black,bold on ;borders: top_color black ,bottom_color green, right_color pink , left_color green,left thin ,right thick , bottom thick , top thin;pattern:pattern solid ,fore_color aqua')
#
# sheet1.col(0).width = 7000
# sheet1.write(0, 0, self.name, format1)
#
# stream = BytesIO()
# workbook.save(stream)
# out = base64.encodebytes(stream.getvalue())
#
# excel_id = self.env["custom.excel.class"].create({"datas_fname": filename, "file_name": out})
#
# return {
#     "res_id": excel_id.id,
#     "name": 'Staff Report',
#     'view_type': 'form',
#     'res_model': "custom.excel.class",
#     'view_id': False,
#     'type': "ir.actions.act_window"
#
# }

class PracticeOdoo(models.Model):
    _name = 'model.info'
    _description = 'Odoo Practice'
    _rec_name = 'name'
    _order = ('dob desc')
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def new_field(self):
        print(" executed a function by object button")

    def resignation(self):
        for rec in self:
            rec.status = 'resign'

    def revert_to_active(self):
        for rec in self:
            rec.status = 'active'

    name = fields.Char(string="Name", track_visibility="always")
    dob = fields.Date(string="DOB")
    country = fields.Many2one('res.country', string="country")
    country_ids = fields.Many2many('res.country', string="country_id")
    country_code = fields.Char(string="country_code", related="country.code")
    sequence = fields.Integer(string="Seq.")
    mobile = fields.Char(string="Mobile", default="1234567890")
    age = fields.Integer(string="Age")

    status = fields.Selection([('active', "Active"), ('resign', "Resign")], string="status", readonly=True,
                              default='active')
    gender = fields.Selection([('male', "Male"), ('female', 'Female')], string="gender")
    hand_salary = fields.Float(string="In Hand Salary")
    epf_esi = fields.Float(string="EPF+ESI")
    ctc_salary = fields.Float(string="CTC", compute="calc_ctc")

    def action_email_template(self):
        # template_id = self.env.ref('school.mail_template_blog')  # Replace 'your_module.email_template_id' with the actual ID of your email template
        # # template_id.send_mail(self.id, force_send=True)
        # self.ensure_one()
        # # self.order_line._validate_analytic_distribution()
        # lang = self.env.context.get('lang')
        # mail_template = self.env.ref('practice.mail_template_blog')
        # if mail_template and mail_template.lang:
        #     lang = mail_template._render_lang(self.ids)[self.id]
        # ctx = {
        #     'default_model': 'sale.order',
        #     'default_res_ids': self.ids,
        #     'default_template_id': mail_template.id if mail_template else None,
        #     'default_composition_mode': 'comment',
        #     'mark_so_as_sent': True,
        #     'default_email_layout_xmlid': 'mail.mail_notification_layout_with_responsible_signature',
        #     'proforma': self.env.context.get('proforma', False),
        #     'force_email': True
        #
        # }
        # return {
        #     'type': 'ir.actions.act_window',
        #     'res_model': 'mail.compose.message',
        #     'view_mode': 'form, tree',
        #     'views': [(False, 'form')],
        #     'view_id': False,
        #     'target': 'new',
        #     'context': ctx
        # }
        pass

    # class RestStaffLine(models.Model):


    @api.depends('hand_salary', 'epf_esi')
    def calc_ctc(self):
        for record in self:
            ctc = 0
            if record.hand_salary:
                ctc = ctc + record.hand_salary
            if record.epf_esi:
                ctc = ctc + record.epf_esi
            record.ctc_salary = ctc


    @api.constrains('mobile')
    def _check_mobile_number_length(self):
        for record in self:
            if record.mobile and len(record.mobile) < 10:
                raise ValidationError(_("Mobile number should be more than 10 digits."))


    @api.constrains('age')
    def val_age(self):
        for rec in self:
            if rec.age and rec.age < 18:
                raise ValidationError(_("u r not valid"))



#     _name = 'rest.staff.line'
#
#
#     connecting_field = fields.Many2one('model.info',string =  'connecting field')
#     last_name = fields.Char(string= "last_name")
#     product_id = fields.Many2many("product.product",string = "product_id")
class CustomExcel(models.TransientModel):
    _name = 'custom.excel.class'
    _rec_name = "datas_fname"

    file_name = fields.Binary(string="Report")
    datas_fname = fields.Char(string="filename")

    start_date = fields.Date(string="start_date")
    end_date = fields.Date(string="end_date")

    def print_excel(self):
        start = self.start_date
        end = self.end_date
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        sheet = workbook.add_worksheet('Transactions')

        bold_format = workbook.add_format(
            {'bold': True, 'align': 'center', 'font_size': 10, 'valign': 'vcenter', 'bg_color': '#f2eee4',
             'border': True})
        normal_format = workbook.add_format({'text_wrap': True, 'align': 'center', 'valign': 'top'})
        number_format = workbook.add_format({'text_wrap': True, 'align': 'right', 'valign': 'top'})
        date_format = workbook.add_format({'num_format': 'dd/mm/yy', 'align': 'center'})
        sheet.set_column('A:G', 12)  # Adjust the width as needed
        # Set row height
        sheet.set_default_row(30)  # Adjust the height as needed
        row = 1
        col = 0
        data = self.env["sale.order"].search([('date_order', '>', start),
                                              ('date_order', '>', end)])
        # record = self.env['sale.order'].browse(data)

        # Write headers with bold format
        sheet.write('A1', 'Number', bold_format)
        sheet.write('B1', 'Date', bold_format)
        sheet.write('C1', 'Status', bold_format)
        sheet.write('D1', 'Total', bold_format)
        sheet.write('E1', 'Name', bold_format)

        # row += 1
        for rec in data:
            sheet.write(row, col, rec.name or '',
                        number_format)  # Changed rec.name to rec.name or '' to avoid NoneType error
            sheet.write(row, col + 1, rec.date_order.strftime('%Y-%m-%d') if rec.date_order else '', date_format)
            sheet.write(row, col + 2, rec.invoice_status or '', normal_format)
            sheet.write(row, col + 3, rec.amount_total or 0.0, normal_format)
            sheet.write(row, col + 4, rec.user_id.name or 'NA', normal_format)
            row += 1

        workbook.close()
        output.seek(0)

        # Encode the file to base64
        excel_file = base64.b64encode(output.read())
        output.close()

        # Create an attachment
        attachment = self.env['ir.attachment'].create({
            'name': f'{self.customer.name}_report.xlsx',  # Changed from f'{self.name}_report.xlsx'
            'type': 'binary',
            'datas': excel_file,
            'res_model': 'commission.model',
            'res_id': self.id,
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        })

        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'self',
        }
