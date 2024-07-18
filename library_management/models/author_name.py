from odoo import models, fields


class AuthorInformation(models.Model):
    _name = "author.info"
    _description = "this model is about Author Information"

    author_name = fields.Char(string="Author_Name", required=True)
    about_author = fields.Text(string="About_Author")
    author_dob = fields.Date(string="Author_DOB")
    author_gender = fields.Selection( [('male', "Male"),("female","Female")] ,string = "Gender")
