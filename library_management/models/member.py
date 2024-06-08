from odoo import models, fields

class MemberInformation(models.Model):
    _name = "member.info"
    _description = "this model is about member Information"

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Integer(string='Phone')
    address = fields.Text(string='Address')

class JavascriptFunction(models.Model):
    _inherit = 'sale.order'


class SaleOrderLines(models.Model):
    _inherit = "hr.expense"

    def print_report(self):
        print("<<<<<<<<<<<<>>>>>>>>>>>>",self.ids)
        # if len(self.ids) < 1:
        #     data = self.env["hr.expense"].search([])
        #     print(data)
        #     action = self.env.ref('library_management.action_hr_expense').with_context(my_report = True, order_lines = data).report_action(data)
        #     return action
        # else:
        #     action = self.env.ref('library_management.action_hr_expense').with_context(my_report = True, order_lines = self).report_action(self)
        #     return action
        #
