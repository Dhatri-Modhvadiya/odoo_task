from odoo import fields, models, api
import io
import xlsxwriter
import xlrd
import base64

from odoo.exceptions import ValidationError


class Print(models.TransientModel):
    _name = "xlreport.wizard"

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    def submit(self):
        currency_symbol = self.env.user.company_id.currency_id.symbol
        start = self.start_date
        end = self.end_date
        if start > end:
            raise ValidationError("The start date cannot be later than the end date.")

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        sheet = workbook.add_worksheet('customer')
        sheet2 = workbook.add_worksheet('Employee')

        bold_format = workbook.add_format({
            'bold': 600,
            'align': 'center',
            'valign': 'center',
            'font_size': 11,
            'bg_color': '#FFA500',
            'border': True
        })
        normal_format = workbook.add_format({
            'text_wrap': True,
            'valign': 'center',
            'align': 'center',
            'font_size': 10
        })
        number_format = workbook.add_format({
            'text_wrap': True,
            'align': 'right',
            'font_size': 9
        })
        text_format = workbook.add_format({
            'text_wrap': True,
            'align': 'left',
            'font_size': 10
        })
        date_format = workbook.add_format({
            'num_format': 'dd/mm/yy',
            'align': 'center',
            'font_size': 10
        })

        # Define a format for the merged cells
        merge_format = workbook.add_format({
            'bold': True,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'yellow',  # Example: setting a background color
            'border': 1
        })


        # Merge cells from first row and first column to first row and third column
        sheet.merge_range('A10:C10', 'Merged Cells', merge_format)


        dollar_format = workbook.add_format({'num_format': '$#,##0.00', "font_size": 10})
        sheet.set_column('A:I', 15)  # Adjust the width as needed
        # sheet.set_column('J:J',40)
        sheet.set_default_row(25)  # Adjust the height as needed

        # cell_format = workbook.add_format({'bg_color': 'green'})  # You can change the color here

        sheet.write('A1', 'Number', bold_format)
        sheet2.write('A1', 'Number', bold_format)
        sheet.write('B1', 'Date', bold_format)
        sheet.write('C1', "Expire Date", bold_format)
        sheet.write('D1', 'Status', bold_format)
        sheet.write('E1', "Invoice Statue", bold_format)
        sheet.write('F1', 'Sale Team', bold_format)
        sheet.write('G1', 'Name', bold_format)
        sheet.write('H1', 'Company', bold_format)
        sheet.write('I1', 'Tags', bold_format)
        sheet.write('J1', 'UnTaxes', bold_format)
        sheet.write('K1', 'Taxes', bold_format)
        sheet.write('L1', 'Total', bold_format)

        col = 0
        row = 1
        data = self.env['sale.order'].search([('date_order', '>=', start), ('date_order', '<=', end)])

        for rec in data:
            sheet.write(row, col, rec.name or '', normal_format)
            sheet2.write(row, col, rec.name or '', normal_format)
            sheet.write(row, col + 1, rec.date_order.strftime('%Y-%m-%d') if rec.date_order else '', date_format)
            sheet.write(row, col + 2, rec.validity_date.strftime('%Y-%m-%d') if rec.date_order else '', date_format)
            sheet.write(row, col + 3, rec.state or '', normal_format)
            sheet.write(row, col + 4, rec.invoice_status or '', normal_format)

            sheet.write(row, col + 5, rec.team_id.name or 0.0, text_format)
            sheet.write(row, col + 6, rec.user_id.name or 'NA', text_format)
            sheet.write(row, col + 7, rec.partner_id.name or 'NA', text_format)

            tag_names = ', '.join(rec.tag_ids.mapped('name'))
            sheet.write(row, col + 8, tag_names or 'NA', normal_format)
            sheet.write(row, col + 9, rec.amount_untaxed or 'NA', dollar_format)
            sheet.write(row, col + 10, rec.amount_tax or 'NA', dollar_format)
            sheet.write(row, col + 11, rec.amount_total or 'NA', dollar_format)
            row += 1

            #

            sheet1 = workbook.add_worksheet('Sales')
            sheet1.merge_range('A10:C10', 'Merged Cells', merge_format)

            bold_format = workbook.add_format({
                'bold': True, 'align': 'center', 'font_size': 10, 'valign': 'vcenter',
                'bg_color': '#FF5733', 'border': True, 'text_wrap': True
            })
            header_format = workbook.add_format({
                'bold': True, 'align': 'center', 'font_size': 12, 'valign': 'vcenter',
                'bg_color': '#FFEB3B', 'font_color': '#FFFFFF', 'border': True, 'text_wrap': True
            })
            normal_format = workbook.add_format({
                'text_wrap': True, 'align': 'left', 'valign': 'top', 'border': True
            })
            number_format = workbook.add_format({
                'num_format': '0.00', 'text_wrap': True, 'align': 'left', 'valign': 'top', 'border': True
            })
            total_format = workbook.add_format({
                'bold': True, 'bg_color': '#FFEB3B', 'border': True  # Yellow background for totals
            })

            sheet1.set_column('A:A', 20)
            sheet1.set_column('B:E', 15)
            sheet1.set_default_row(20)
            sheet1.set_row(0, 30)

            # sheet1.merge_range('A1:F1')
            sheet1.set_row(0, 25)  # Set row height for the header
            sheet1.set_row(1, 30)

            # Write headers with bold format
            headers = [
                'Customer', 'Untaxed amount', 'Taxes', 'Amount Total', 'Amount to invoice', 'Total'
            ]
            # for i, header in enumerate(headers):
            #     sheet1.write(1, i, header, bold_format)

            # domain = [
            #     ('date_order', '>=', self.start_date),
            #     ('date_order', '<=', self.end_date),
            # ]
            # customer_data = self.env['sale.order'].read_group(domain, ['amount_untaxed', 'amount_tax', 'amount_total', 'amount_to_invoice'], ['partner_id'])
            # row = 2  # Start from the third row

            for i, header in enumerate(headers):
                sheet1.write(1, i, header, bold_format)

            query = """
            SELECT so.partner_id, 
                   SUM(so.amount_untaxed) AS amount_untaxed,
                   SUM(so.amount_tax) AS amount_tax,
                   SUM(so.amount_total) AS amount_total,
                   SUM(so.amount_to_invoice) AS amount_to_invoice
                FROM sale_order so
                WHERE so.date_order >= %s AND so.date_order <= %s
                GROUP BY so.partner_id
            """
            self.env.cr.execute(query, (self.start_date, self.end_date))
            results = self.env.cr.fetchall()

            row = 2  # Start from the second row for data
            for result in results:
                partner_id = result[0]
                amount_untaxed = result[1]
                amount_tax = result[2]
                amount_total = result[3]
                amount_to_invoice = result[4]

                # Get partner name using partner_id
                partner_name = self.env['res.partner'].browse(partner_id).name

                # Write data to the worksheet
                sheet1.write(row, 0, partner_name, normal_format)
                sheet1.write(row, 1, f"{currency_symbol}{round(amount_untaxed, 2)}", number_format)
                sheet1.write(row, 2, f"{currency_symbol}{round(amount_tax, 2)}", number_format)
                sheet1.write(row, 3, f"{currency_symbol}{round(amount_total, 2)}", number_format)
                sheet1.write(row, 4, f"{currency_symbol}{round(amount_to_invoice, 2)}", number_format)

                row += 1

            # for rec in customer_data:
            #     partner_name = self.env['res.partner'].browse(rec['partner_id'][0]).name
            #     amount_untaxed = rec.get('amount_untaxed', 0)
            #     amount_tax = rec.get('amount_tax', 0)
            #     amount_total = rec.get('amount_total', 0)
            #     amount_to_invoice = rec.get('amount_to_invoice', 0)

            #     sheet1.write(row, 0, partner_name, normal_format)
            #     sheet1.write(row, 1, f"{currency_symbol}{amount_untaxed or 'NA'}", number_format)
            #     sheet1.write(row, 2, f"{currency_symbol}{amount_tax or 'NA'}", number_format)
            #     sheet1.write(row, 3, f"{currency_symbol}{amount_total or 'NA'}", number_format)
            #     sheet1.write(row, 4, f"{currency_symbol}{amount_to_invoice or 'NA'}", number_format)
            #     row+=1

            workbook.close()
            output.seek(0)

            # Encode the file to base64
            excel_file = base64.b64encode(output.read())
            output.close()

            # Create an attachment
            attachment = self.env['ir.attachment'].create({
                'name': f'sales_report_from_{self.start_date}_to_{self.end_date}.xlsx',
                'type': 'binary',
                'datas': excel_file,
                'res_model': 'commission.sale.wizard',
                'res_id': self.id,
                'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            })

            return {
                'type': 'ir.actions.act_url',
                'url': f'/web/content/{attachment.id}?download=true',
                'target': 'self'
            }

        #
        workbook.close()
        output.seek(0)

        # Encode the file to base64
        excel_file = base64.b64encode(output.read())
        output.close()

        # Create an attachment
        attachment = self.env['ir.attachment'].create({
            'name': f'Sale_report.xlsx',
            'type': 'binary',
            'datas': excel_file,
            'res_model': 'sale.order',
            'res_id': self.id,
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        })

        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'self',
        }
