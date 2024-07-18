from odoo import http
from odoo.http import request

class CyberSourceController(http.Controller):
    _inherit= "payment.provider"

    @http.route('/payment/cybersource/return', type='http', auth='public', csrf=False)
    def cybersource_return(self, **kwargs):
        # Handle the return URL from CyberSource
        payment_provider = request.env['payment.provider'].sudo().search([('provider', '=', 'cybersource')], limit=1)
        if payment_provider:
            payment_provider._cybersource_confirm_payment(kwargs.get('payment_id'))
        return request.redirect('/payment/status')

    @http.route('/payment/cybersource/cancel', type='http', auth='public', csrf=False)
    def cybersource_cancel(self, **kwargs):
        # Handle the cancellation URL from CyberSource
        return request.redirect('/payment/status')
