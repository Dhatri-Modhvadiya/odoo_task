from odoo import models
import requests
import json
import datetime
import hmac
import hashlib
import base64



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def capture_payment_cybersource(self, payments_need_tx=None):
        self.ensure_one()
        order = self

        # Debugging: print the order details
        print(f"Order ID: {order.id}")
        print(f"Order Total Amount: {order.amount_total}")
        print(f"Order Currency: {order.currency_id.name}")

        url = "https://apitest.cybersource.com/pts/v2/payments"
        payload = {
            "clientReferenceInformation": {
                "code": "TC50171_3"
            },
            "paymentInformation": {
                "card": {
                    "number": "4111111111111111",
                    "expirationMonth": "12",
                    "expirationYear": "2031"
                }
            },
            "orderInformation": {
                "amountDetails": {
                    # printing the amount from the sale order
                    "totalAmount": str(order.amount_total),
                    "currency": order.currency_id.name
                },
                #     "totalAmount": "102.21",
                #     "currency": "USD"
                # },
                "billTo": {
                    "firstName": "John",
                    "lastName": "Doe",
                    "address1": "1 Market St",
                    "locality": "san francisco",
                    "administrativeArea": "CA",
                    "postalCode": "94105",
                    "country": "US",
                    "email": "admin@example.com",
                    "phoneNumber": "4158880000"
                }
            }
        }

        print('totalAmount')

        # Prepare the headers
        merchant_id = "dhatri8203_1720526956"
        key_id = '4c595c7b-39cc-44e1-980e-2e97974486c8'
        secret_key = 'Q7GLlxVJ1V6s7QEAhxhr6LooOAQUs1yx77KD1S0oA9E='
        timestamp = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        digest = base64.b64encode(hashlib.sha256(json.dumps(payload).encode('utf-8')).digest()).decode('utf-8')

        signature_header = f"host: apitest.cybersource.com\nv-c-date: {timestamp}\nrequest-target: post /pts/v2/payments\ndigest: SHA-256={digest}\nv-c-merchant-id: {merchant_id}"

        signature = base64.b64encode(
            hmac.new(base64.b64decode(secret_key), signature_header.encode('utf-8'), hashlib.sha256).digest()
        ).decode('utf-8')

        signature = f'keyid="{key_id}", algorithm="HmacSHA256", headers="host v-c-date request-target digest v-c-merchant-id", signature="{signature}"'

        headers = {
            'host': "apitest.cybersource.com",
            'v-c-date': timestamp,
            'digest': f"SHA-256={digest}",
            'v-c-merchant-id': merchant_id,
            'signature': signature,
            'Content-Type': 'application/json'
        }

        response = requests.post(url, json=payload, headers=headers)
        print("response created", response)

        if response.status_code == 201:
            self.message_post(body="Payment successfully captured via CyberSource.")
            self._create_invoices()
            self._create_payment_transaction()
            csTrans = payments_need_tx.sudo()._create_payment_transaction()
            # transactions = payments_need_tx.sudo()._create_payment_transaction()

        else:
            self.message_post(body=f"Failed to capture payment: {response.text}")

        return True


