from odoo import models, fields

class MailTemplate(models.Model):
    _inherit = 'mail.template'

    recipient_category = fields.Selection([('practitioner', 'Practitioner'), ('administrative', 'Administrative'), ('client', 'Client')], required=True, string='Recipient Category')
    create_memo = fields.Boolean(string='Create Memo')