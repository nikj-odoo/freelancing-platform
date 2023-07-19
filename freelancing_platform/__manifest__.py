{
    'name' : 'Freelancing ',
    'summary': "Freelancing Platform",
    'author': "Odoo",
    'version': '1.0',
    'description':""" This is the module for self learing""",
    'category': 'Industry',
    'depends' : ['mail','contacts'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'website': 'https://www.odoo.com/',
    
    #'depends' : ['base_setup', 'product', 'analytic', 'portal', 'digest'],
    'application': True,
    'installable':True,
    
    'data':[
        'security/ir.model.access.csv',
        'data/data_seq.xml',
        'views/freelancing_platform_offers.xml',
        'views/freelancing_platform_types.xml',
        'views/freelancing_platform_skills.xml',
        'views/freelancing_view.xml'
        
        ]
}
