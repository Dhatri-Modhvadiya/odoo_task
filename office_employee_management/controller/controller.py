from odoo import http
from odoo.http import request
import json


class SaleOrderController(http.Controller):

    @http.route('/create_sale_order', type='json', auth='public', methods=['POST'], csrf=False)
    def create_sale_order(self, **kwargs):
        try:
            # Extract data from the request
            data = json.loads(request.httprequest.data)

            # Define sale order values
            order_vals = {
                'partner_id': data.get('partner_id'),
                'order_line': [(0, 0, {
                    'product_id': line.get('product_id'),
                    'product_uom_qty': line.get('quantity'),
                    'price_unit': line.get('price_unit'),
                }) for line in data.get('order_lines', [])]
            }

            # Create the sale order
            sale_order = request.env['sale.order'].sudo().create(order_vals)

            return {'status': 'success', 'sale_order_id': sale_order.id}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}



class Controller(http.Controller):

    @http.route('/office/employee/',website = True ,auth = 'public')

    def check_controller(self,**kwargs):
        # return "hello , odoo!"
        return request.render("office_employee_management.office_data",{})


