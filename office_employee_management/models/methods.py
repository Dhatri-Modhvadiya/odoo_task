from odoo import models, fields, api
class MethodModel(models.Model):
    # Attributes
    _name = "method.info"
    _description = "orm methods"

    # fields
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    # manager = fields.Char(string="Manager")
    # employee_ids = fields.Integer(string="Employee_Id")




    @api.model
    def create(self,values):
        print("values of create method",values)
        print("self",self)
        rtn = super(MethodModel,self).create(values)
        print("return statement ",rtn)
        return rtn






