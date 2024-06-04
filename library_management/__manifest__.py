{
    "name": "library info",
    "author": "Dhatri",
    "version": "1.0.0",
    "sequence": -100,
    "category": "Library Management",
    "website": "www.library.comc",
    "summary": "This module is about library management system , which gives us details about the records",
    "depends": ['base', 'web', 'hr_expense','sale','sale_management','point_of_sale'],
    "data": ["security/ir.model.access.csv",
             "views/menu.xml",
             "views/author_name_view.xml",
             "views/book_view.xml",
             "views/browsing_history_view.xml",
             "views/member_view.xml", ],
    'assets': {
        'web.assets_backend': [
            'library_management/static/src/xml/hr_expense.xml',
            'library_management/static/src/js/custom_list_button.js'
        ],
    },

}
