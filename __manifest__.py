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
        'views/mail_template_views.xml',
        'views/mail_compose_message_views.xml',
        'views/memo_menus.xml',
       # 'report/action_memo_report.xml',
       # 'report/memo_log_report_templates.xml',
        'data/mail_template.xml'
    ],

}

