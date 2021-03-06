# -*- coding: utf-8 -*-
{
    'name': "condominium_frontend",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/layout.xml',
        # 'views/pages.xml',
        
        'views/assets.xml',
        'views/footer.xml',
        'views/pages/home.xml',
        'views/pages/contactus.xml',
        'views/pages/features.xml',
        'views/pages/pricing.xml',
        'views/pages/services.xml',
        'views/pages/login.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}