{
    'name': 'Multi-Department Project Management',
    'version': '1.0',
    'summary': 'Monitor projects across multiple departments',
    'description': """
        This module allows you to create and monitor projects that involve multiple departments.
        Features:
        - Create departments with their own members and tasks
        - Monitor project progress across departments
        - Assign tasks to specific departments
    """,
    'category': 'Project',
    'author': 'rfahur11',
    'website': 'https://www.example.com',
    'depends': ['base', 'project', 'hr'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/department_views.xml',
        'views/project_views.xml',
        'views/task_views.xml',
        'views/member_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}