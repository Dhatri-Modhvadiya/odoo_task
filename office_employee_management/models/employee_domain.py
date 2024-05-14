import self
from odoo import models, fields, api
from odoo.exceptions import ValidationError



class Employee_domain(models.Model):
    # Attributes
    _name = 'domain.info'
    _description = 'Employee domain'
    _rec_name = "employee_size"


    # fields
    employee_size = fields.Integer(string="Employee_Size")
    allocated_floor = fields.Char(string='Allocated_Floor', index=True)
    tl_name = fields.Char(string='TL_Name', required=True)
    domain_selection = fields.Selection([('odoo', 'Odoo'), ('Shopify', 'shopify'), ( 'magento','Magento'), ('php', 'Php'),('others','Others')], string='domain selection',default='php')

    # field for smart button
    listed_property_count = fields.Integer(string='Listed Property Count', compute='_compute_listed_property_count')

    # function for smart button start here
    def action_order_list(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'domain',
            'res_model': 'domain.info',
            'view_mode': 'tree,form',
            'target': 'new',
            'domain': [('domain_selection', '=', self.domain_selection)]
        }
    @api.depends('domain_selection')
    def _compute_listed_property_count(self):
        for record in self:
            listed_property_count = self.env['domain.info'].search_count(
                [('domain_selection', '=', record.domain_selection)])
            record.listed_property_count = listed_property_count

    # function for smart button end here


    @api.model
    def create(self, vals):
        res = super(Employee_domain, self).create(vals)
        print("created values is :", vals)
        return res
    def unlink(self):
        if self.domain_selection == 'odoo':
            raise ValidationError("You cannot delete odoo domain")
        res = super(Employee_domain, self).unlink()
        return res

    def write(self,vals):
        res = super(Employee_domain,self).write(vals)

        print("Write method is triggered",vals)
        return res

    def copy(self,default = None):
        if self.domain_selection == 'odoo':
            raise ValidationError("You cannot duplicate the record")
        res = super(Employee_domain, self).copy(default)
        return res