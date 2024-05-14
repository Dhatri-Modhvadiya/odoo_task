# -*- coding: utf-8 -*-
{
    'name': 'Office Employee Management',
    'version': '1.0.0',
    'category': 'employee',
    'author':'Brainvire Infotech',
    'sequence' : -400 ,
    'summary': 'office employee management system',
    'description': """""Office Employee Management""",
    'depends': ['base','sale','sale_management','stock'],
    'data': ["security/ir.model.access.csv",
             "data/sequence_view.xml",
             "wizard/demo.xml",
             "views/menu.xml",
             "views/employee_info.xml",
             "views/salary.xml",
             "views/employee_domain.xml",
             "views/leave_management.xml",
             "views/department.xml",
             "reports/emp_management_report.xml",
             "reports/department_report.xml"
    ],
    'demo': [],
    'installable': True,
    'auto_install' : False,
    'license': 'LGPL-3',
    'assets': {}
}