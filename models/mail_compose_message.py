from odoo import models, fields

class MailComposeMessage(models.Model):
    _inherit = 'mail.compose.message'

    recipient_category = fields.Selection([
        ('practitioner', 'Practitioner'),
        ('administrative', 'Administrative'),
        ('client', 'Client')
    ], required=True, string='Recipient Category')
    create_memo = fields.Boolean(string='Create Memo')
