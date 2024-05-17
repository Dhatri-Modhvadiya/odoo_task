from odoo import models,fields,api,_
from odoo.exceptions import ValidationError

from odoo17.odoo import exceptions


class PracticeOdoo(models.Model):
    _name = 'model.info'
    _description = 'Odoo Practice'
    _rec_name = 'name'
    _order = ('dob desc')
    _inherit =['mail.thread','mail.activity.mixin']



    def new_field(self):
        print(" executed a function by object button")

    def resignation(self):
        for rec in self:
            rec.status = 'resign'

    def revert_to_active(self):
        for rec in self:
            rec.status = 'active'


    name = fields.Char(string = "Name",track_visibility = "always")
    dob = fields.Date(string = "DOB")
    country = fields.Many2one('res.country',string="country")
    country_ids = fields.Many2many('res.country', string = "country_id")
    country_code =  fields.Char(string = "country_code" , related = "country.code")
    sequence = fields.Integer(string = "Seq.")
    mobile = fields.Char(string = "Mobile",default = "1234567890")
    age = fields.Integer(string = "Age")

    status = fields.Selection([('active',"Active"),('resign',"Resign")],string = "status",readonly = True,default = 'active')
    gender = fields.Selection([('male',"Male"),('female','Female')],string ="gender")
    hand_salary = fields.Float(string = "In Hand Salary")
    epf_esi = fields.Float(string = "EPF+ESI")
    ctc_salary = fields.Float(string = "CTC" , compute = "calc_ctc")


    @api.depends('hand_salary','epf_esi')
    def calc_ctc(self):
        for record in self:
            ctc = 0
            if record.hand_salary:
                ctc = ctc +record.hand_salary
            if record.epf_esi:
                ctc = ctc +record.epf_esi
            record.ctc_salary = ctc


    @api.constrains('mobile')
    def _check_mobile_number_length(self):
        for record in self:
            if record.mobile and len(record.mobile) < 10:
                raise ValidationError(_("Mobile number should be more than 10 digits."))



    @api.constrains('age')
    def val_age(self):
        for rec in self:
            if rec.age and rec.age < 18 :
                raise ValidationError(_("u r not valid"))

    def action_email_template(self):

        # template_id = self.env.ref('school.mail_template_blog')  # Replace 'your_module.email_template_id' with the actual ID of your email template
        # template_id.send_mail(self.id, force_send=True)
        self.ensure_one()
        # self.order_line._validate_analytic_distribution()
        lang = self.env.context.get('lang')
        mail_template = self.env.ref('practice.mail_template_blog')
        if mail_template and mail_template.lang:
            lang = mail_template._render_lang(self.ids)[self.id]
        ctx = {
            'default_model': 'sale.order',
            'default_res_ids': self.ids,
            'default_template_id': mail_template.id if mail_template else None,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'default_email_layout_xmlid': 'mail.mail_notification_layout_with_responsible_signature',
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

    # class RestStaffLine(models.Model):
    #     _name = 'rest.staff.line'
    #
    #
    #     connecting_field = fields.Many2one('model.info',string =  'connecting field')
    #     last_name = fields.Char(string= "last_name")
    #     product_id = fields.Many2many("product.product",string = "product_id")

