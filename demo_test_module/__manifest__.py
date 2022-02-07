# -*- coding: utf-8 -*-
{
    'name': "Automated Test Demo",

    'summary': """
        Automated Test Demo""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Syarif Hidayatullah",
    'maintainer': 'ERP Team',
    'website': "http://www.warungpintar.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.0',

    # any module necessary for this one to work correctly
    'depends': ['material'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}