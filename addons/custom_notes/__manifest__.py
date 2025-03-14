{
    'name': 'Custom Notes',
    'version': '1.0',
    'summary': 'Simple Notes Module with Title and Date',
    'description': 'A module to create and manage notes with title and date fields',
    'category': 'Tools',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_notes_views.xml',
        'views/custom_notes_menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}