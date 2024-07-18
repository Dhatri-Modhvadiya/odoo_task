from odoo import models, fields, api, _
import requests

class PaymentProvider(models.Model):
    _inherit = 'payment.provider'


    provider = fields.Selection([('cybersource', 'CyberSource')], ondelete={'cybersource': 'set default'},string="Provider")
    cybersource_api_key = fields.Char(string='CyberSource API Key', required_if_provider='cybersource')
    cybersource_merchant_id = fields.Char(string='CyberSource Merchant ID', required_if_provider='cybersource')
    cybersource_secret_key = fields.Char(string='CyberSource Secret Key', required_if_provider='cybersource')

    def _cybersource_get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.cybersource_api_key}'
        }

    def _cybersource_create_payment(self, amount, currency):
        # url = 'https://api.cybersource.com/payments/v1/payments'
        url ='https://apitest.cybersource.com/pts/v2/payments'

        payload = {
            "amount": amount,
            "currency": currency,
            "merchant_id": self.cybersource_merchant_id,
            "reference_number": "OdooPayment",
            # Additional CyberSource-specific parameters
        }
        headers = self._cybersource_get_headers()
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()

    def _cybersource_confirm_payment(self, payment_id):
        url = f'https://api.cybersource.com/payments/v1/payments/{payment_id}/confirm'
        headers = self._cybersource_get_headers()
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return response.json()
