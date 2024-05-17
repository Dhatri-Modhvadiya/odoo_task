# -*- coding: utf-8 -*-
{
    'name': 'Practice  Management',
    'version': '1.0.0',
    'category': 'practice',
    'author':'Dhatri ',
    'sequence' : -400 ,
    'summary': 'just for practice',
    'description': """""""",
    'depends': ['base','mail','sale','stock'],
    'data': ["security/ir.model.access.csv",
             "data/pratice_email_template.xml",
             "data/res_partner_template.xml",
             "wizard/wizard_practice_view.xml",
             "views/menu.xml",
             "views/practice.xml",
             "views/email_template.xml",
             "report/email_template_report.xml"
           ],
    'demo': [],
    'installable': True,
    'auto_install' : False,
    'license': 'LGPL-3',
    'assets': {}
}