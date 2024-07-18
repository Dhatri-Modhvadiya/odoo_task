from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('order_line')
    def _compute_order_lines_stats(self):
        self.order_lines_count = len(self.order_line)
        self.order_lines_total = sum(line.price_subtotal for line in self.order_line)

    @api.depends('amount_total', 'partner_id')
    def _compute_sales_stats(self):
        total_sales = self.env['sale.order'].search_count([('partner_id', '=', self.partner_id.id)])
        average_order_amount = self.amount_total / total_sales if total_sales else 0.0
        self.total_sales = total_sales
        self.average_order_amount = average_order_amount

    order_lines_count = fields.Integer(string='Order Lines Count', compute='_compute_order_lines_stats')
    order_lines_total = fields.Monetary(string='Order Lines Total', compute='_compute_order_lines_stats')
    total_sales = fields.Integer(string='Total Sales', compute='_compute_sales_stats')
    average_order_amount = fields.Monetary(string='Average Order Amount', compute='_compute_sales_stats')

    def action_view_order_lines(self):
        # Define your action method to show order lines
        # Example: return an action to open a tree view of order lines related to this sale order
        return {
            'type': 'ir.actions.act_window',
            'name': 'Order Lines',
            'view_mode': 'tree,form',
            'res_model': 'sale.order.line',
            'domain': [('order_id', '=', self.id)],
        }

    def action_view_sales_stats(self):
        # Define your action method to show sales stats
        # Example: return an action to display sales statistics
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sales Stats',
            'view_mode': 'form',
            'res_model': 'sale.order',
            'res_id': self.id,
            'target': 'new',
        }
