# -*- coding: utf-8 -*-
{
    'name': 'Office Employee Management',
    'version': '1.0.0',
    'category': 'employee',
    'author':'Brainvire Infotech',
    'sequence' : -400 ,
    'summary': 'office employee management system',
    'description': """""Office Employee Management""",
    'depends': ['base', 'sale', 'stock', 'sale_management', 'mail', 'web', 'hr_expense'],
    'data': ["security/ir.model.access.csv",
             "security/access_rights.xml",
             "data/sequence_view.xml",
             "data/email_template.xml",
             "data/cron.xml",
             "data/monthly_report.xml",
             "wizard/demo.xml",
             "wizard/excel_report.xml",
             "views/menu.xml",
             "views/employee_info.xml",
             # "views/methods.xml",
             # "views/salary.xml",
             "views/employee_domain.xml",
             "views/leave_management.xml",
             "views/department.xml",
             # "views/custom_widget_template.xml",
             # "views/hr_expense.xml",
             # "views/assets.xml",
             "reports/emp_management_report.xml",
             "reports/department_report.xml",
    ],
    'assets': {
        'web.assets_backend': [
        #     'library_management/static/src/js/custom_class.js',
        #     'office_employee_management/static/src/js/department.js'
        ],


    },
    'demo': [],
    'installable': True,
    'auto_install' : False,
    'license': 'LGPL-3',
    'assets': {}
}