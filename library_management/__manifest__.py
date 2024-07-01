{
    "name": "library info",
    "author": "Dhatri",
    "version": "1.0.0",
    "sequence": -100,
    "category": "Library Management",
    "website": "www.library.comc",
    "summary": "This module is about library management system , which gives us details about the records",
    "depends": ['base', 'web', 'hr_expense', 'sale', 'sale_management', 'point_of_sale'],
    "data": ["security/ir.model.access.csv",
             "views/menu.xml",
             "views/author_name_view.xml",
             "views/book_view.xml",
             'views/pos_model.xml',
             # "views/custom_widget_template.xml"
             "views/browsing_history_view.xml",
             "views/member_view.xml",
             # "views/javascript_practice_template.xml",
             # 'views/pos_assets.xml',
             # 'views/custon_note_pos.xml'
             "report/hr_expense_report.xml",
             "report/ir_actions_report.xml"],

    'assets': {
        'web.assets_backend': [
            'library_management/static/src/js/hr_expense.js',
            'library_management/static/src/xml/hr_expense.xml',
            'library_management/static/src/js/javascript_practice.js',
            'library_management/static/src/js/javascript_practice.js',
            'library_management/static/src/js/patch.js',
            'library_management/static/src/js/javascript.js',
            # 'library_management/static/src/xml/javascript_practice.xml',
            # 'library_management/static/src/xml/hr_expense.xml',
            # 'library_management/static/src/js/custom_list_button.js',
            # 'library_management/static/src/js/demo.js'
            # 'library_management/static/src/js/custom_class.js',
            # 'library_management/static/src/js/custom_widget.js,
            # 'library_management/static/src/js/include.js',
        ],

        'web.assets_frontend': [
            'library_management/static/src/js/include.js',
            # 'library_management/static/src/js/practical.js',
        ],
    },



    'assets': {
        'point_of_sale._assets_pos': [
            'library_management/static/src/js/create_button.js',
            'library_management/static/src/js/note_button.js',
            'library_management/static/src/js/discount_button.js',
            'library_management/static/src/xml/pos_button.xml',
            # 'library_management/static/src/xml/pos_notes.xml',
            'library_management/static/src/js/pos_notes.js'
        ],
    }

}
