from odoo import models, fields

class FormData(models.Model):
    _name = 'form.data'
    _description = 'Form Data'

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user.id)


class privateUser(models.Model):
    _name="private.user"
    _inherit = "form.data"