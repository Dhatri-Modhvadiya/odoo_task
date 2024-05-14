# -*- coding: utf-8 -*-
{
    'name': 'Practice  Management',
    'version': '1.0.0',
    'category': 'practice',
    'author':'Dhatri ',
    'sequence' : -400 ,
    'summary': 'just for practice',
    'description': """""""",
    'depends': ['base','mail'],
    'data': ["security/ir.model.access.csv",
             "wizard/wizard_practice_view.xml"
        "views/menu.xml",
        "views/practice.xml",
             ],
    'demo': [],
    'installable': True,
    'auto_install' : False,
    'license': 'LGPL-3',
    'assets': {}
}