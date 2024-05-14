from odoo import models, fields, _, api
from odoo.exceptions import ValidationError

# to inherit sale.order model and add one custom field in it
class StockMoveNew(models.Model):
    _inherit = 'sale.order'
    custom_name = fields.Char(string="Custom Name")

    def action_confirm(self):
        for order in self:
            for line in order.order_line:
                if line.product_uom_qty <= 0:
                    raise ValidationError(
                        "Please enter a quantity value for all order lines before confirming the order.")
        return super(StockMoveNew, self).action_confirm()

    def _get_order_lines_to_report(self):
        # if self._context.get('my_report'):
        #     # pass your lines from here
        #     pass
        # else:
        res = super(StockMoveNew, self)._get_order_lines_to_report()
        print(" res>>>>>>>>>>>>>>", res)
        return res
# -----------------------------------------------------------------------------------------------------


# to inherit stock.picking model and add one custom field in it
class StockMove(models.Model):
    _inherit = 'stock.picking'
    custom_name = fields.Char(related='sale_id.custom_name', string="Custom Name")
# -----------------------------------------------------------------------------------------------------



# to inherit sale.order.line model and add one custom field in it
class StockOrderLineNew(models.Model):
    _inherit = 'sale.order.line'
    extra = fields.Integer(string="Extra Tax")
# -----------------------------------------------------------------------------------------------------



# to inherit stock.move model and add one custom field in it
class StockMovePickingNew(models.Model):
    _inherit = 'stock.move'
    extra = fields.Integer(related='sale_line_id.extra',string="Extra Tax")
# -----------------------------------------------------------------------------------------------------




# to add two fields in res.partner model
class ResPartner(models.Model):
    _inherit = 'res.partner'

    commission_amount = fields.Integer(string = "Commission Amount")
    percentage = fields.Float(string = "percentage")
