{
    'name': 'Master Bank',
    'version': '1.0',
    'summary': 'Master Bank Module',
    'description': 'A module to create and manage master bank data',
    'category': 'Finance',
    'author': 'Gus Khamim',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/master_bank_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}