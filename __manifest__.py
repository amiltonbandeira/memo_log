{
    'name': 'Memo',
    'odoo_version': '18.0',
    'version': '1.0',
    'summary': 'For effective and safe healtcare',
    'description': """memo description """,
    'category': 'Uncategorized',
    'author': 'Alien Group',
    'license': 'LGPL-3',
    'website': '',
    'depends': ['base','project','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/memo_views.xml',
        'views/mail_compose_message_views.xml',
        'views/memo_menus.xml'
       # 'data/mail_templates.xml'
    ],

}

