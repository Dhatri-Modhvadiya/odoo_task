from odoo import models, fields


class Product(models.Model):
    _name = 'example.product'
    _description = 'Product Model'

    name = fields.Char('Name', required=True)
    price = fields.Float('Price')


# def sort_products_by_price():
#     print("helllo")
#     products = [
#         {'name': 'Product A', 'price': 50},
#         {'name': 'Product B', 'price': 30},
#         {'name': 'Product C', 'price': 80},
#     ]
#
#     # Sorting products using lambda function
#     sorted_products = sorted(products, key=lambda x: x['price'])
#
#     # Print the sorted products
#     for product in sorted_products:
#         print(product['name'], product['price'])
#
#     return sorted_products
