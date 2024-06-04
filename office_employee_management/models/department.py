from odoo import models, fields, api

class Department(models.Model):
    # Attributes
    _name = "department.info"
    _description = "Department"

    # fields
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    manager = fields.Many2one('domain.info', string="Manager")
    employee_ids = fields.Many2many('employee.info', string="Employees")

class ResPartner(models.Model):
    _inherit = "res.partner"



    def customerPrint(self):
        return self.env.ref("office_employee_management.action_report_res_partner").report_action(self)
    def action_send_email(self):
        self.ensure_one()
        lang = self.env.context.get('lang')

        # Correct reference to the mail template
        mail_template = self.env.ref('office_employee_management.customer_mail_template_blog')

        if mail_template and mail_template.lang:
            lang = mail_template._render_lang(self.ids)[self.id]

        ctx = {
            'default_model': 'res.partner',  # Use the correct model
            'default_res_ids': [self.id],  # Correct parameter name and as a list
            'default_template_id': mail_template.id if mail_template else None,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'default_email_layout_xmlid': 'mail.mail_notification_light',
            'proforma': self.env.context.get('proforma', False),
            'force_email': True,
        }

        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }

