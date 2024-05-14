from odoo import models, fields, api,_
class Demo(models.Model):
    _name="demo.demo"

    name=fields.Char(string="Name")