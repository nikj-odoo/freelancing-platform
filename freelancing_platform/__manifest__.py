{
    'name' : 'Freelancing ',
    'summary': "Freelancing Platform",
    'author': "Odoo",
    'version': '1.0',
    'description':""" This is the module for self learing""",
    'category': 'Admin/Freelancer',
    'depends' : ['mail','contacts','website'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'website': 'https://www.odoo.com/',
    
    #'depends' : ['base_setup', 'product', 'analytic', 'portal', 'digest'],
    'application': True,
    'installable':True,
    
    'data':[
        'security/freelancing_security.xml',
        'security/ir.model.access.csv',
        'data/data_seq.xml',
        'views/freelancing_platform_offers.xml',
        'wizard/fp_offer_wizard_view.xml',
        'views/inherited_user_view.xml',
        'views/freelancing_platform_types.xml',
        'views/freelancing_platform_skills.xml',
        'views/freelancing_view.xml', 
        'views/menu_web.xml',
        'views/template_controller.xml'
        
        
        ],
    "demo": [
        "demo/freelancing_skills.xml",
        "demo/freelancing_types.xml",
        "demo/fp_view.xml",
    ]
}
