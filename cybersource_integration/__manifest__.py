{
    'name': 'CyberSource Payment Integration',
    'version': '1.0',
    'depends': ["base",'payment','sale','sale_management','account'],
    'data': [
        'security/ir.model.access.csv',
        'data/payment_provider_data.xml',
        'views/payment_provider.xml',
        'views/sale_order_view.xml',
          ],
    'installable': True,
    'auto_install': False,
}
