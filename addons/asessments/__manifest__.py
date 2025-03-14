{
    'name': 'Assessment Management',
    'version': '1.0',
    'summary': 'Manage assessments and assignments',
    'description': 'A module to manage assessments and assign them to users',
    'category': 'Human Resources',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}