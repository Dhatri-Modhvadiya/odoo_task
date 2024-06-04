import self
from odoo import models, fields, api, _


class EmployeeInformation(models.Model):
    # Attributes
    _name = "employee.info"
    _description = "this model is about employee Information"
    _rec_name = "employee_name"

    # function for statusbar start here
    def resignation(self):
        for rec in self:
            rec.status = 'resign'

    def revert_to_active(self):
        for rec in self:
            rec.status = 'active'

    # function for statusbar end here
    # fields
    employee_name = fields.Char(string="Employee_Name", required=True, translate=True)
    emp_position = fields.Selection([('intern', 'Intern'), ('sde', 'SDE'), ('tl', 'TL'), ('pm', 'PM')],
                                    string='emp_position')
    employee_id = fields.Integer(string="Employee_Id", required=True, default=8201)
    employee_dob = fields.Date(string="Emp_DOB")
    employee_salary = fields.Float(string='Salary', digits=(10, 2))
    image = fields.Binary(string="image")
    fresher = fields.Boolean(string="Fresher", help="this is a boolean flag which will hlp")
    # corresponding_technology = fields.Many2many('domain.info', string="Corresponding Technology",domain = [("employee_size",">",'20')])
    status = fields.Selection([('active', "Active"), ('resign', "Resign")], string="status", readonly=True,
                              default='active')

    hand_salary = fields.Float(string="In Hand Salary")
    epf_esi = fields.Float(string="EPF+ESI")
    ctc_salary = fields.Float(string="CTC", compute="calc_ctc")



    @api.depends('hand_salary', 'epf_esi')
    def calc_ctc(self):
        for record in self:
            ctc = 0
            if record.hand_salary:
                ctc = ctc + record.hand_salary
            if record.epf_esi:
                ctc = ctc + record.epf_esi
            record.ctc_salary = ctc

    #name =self.env['employee.info'].search([('employee_name','ilike','D%')])
    @api.model
    def create(self, vals):
        res = super(EmployeeInformation, self).create(vals)
        print("created values is :", vals)
        return res

    def write(self, vals):
        res = super(EmployeeInformation, self).write(vals)
        res1 = self.browse([self.employee_id])
        print("written values is :", vals)
        print("browse values is :", res1)
        res2 = self.search([('employee_id', '=', self.employee_id)])
        print("search values is :", res2)
        return res, res1, res2

    def unlink(self):
        res = super(EmployeeInformation, self).unlink()
        print("created values is :", res)
        return res

    # @api.model
    # def test_cron_job(self):
    #
    #     # print("happy birthday")
    #
    #     # Fetch records that need an email
    #     records = self.search([('email_sent', '=', False)])
    #
    #     # Load the email template
    #     template_id = self.env.ref('office_employee_management.customer_mail_template_blog').id
    #
    #     # Send emails
    #     for record in records:
    #         self.env['mail.template'].browse(template_id).send_mail(record.id, force_send=True)
    #         record.email_sent = True
    #
    # email_sent = fields.Boolean('Email Sent', default=False)
    # print("email template sent")

    # def test_cron_job(self):
    #     today = fields.Date.today()
    #     today_month_day = today.strftime('%m-%d')  # Get the month and day in 'MM-DD' format
    #
    #     records = self.search([])  # Get all records
    #     for rec in records:
    #         if rec.employee_dob and rec.employee_dob.strftime('%m-%d') == today_month_day:  # Compare month and day
    #             email_values = {
    #                 'email_to': rec.email,
    #                 'subject': f"Happy Birthday {rec.display_name}"
    #             }
    #             print(f"Happy Birthday {rec.display_name}")
    #             mail_template = self.env.ref('office_employee_management.customer_mail_template_blog')
    #             mail_template.send_mail(rec.id, email_values=email_values, force_send=True)
    #             print(f"Happy Birthday {rec.display_name} Again")
