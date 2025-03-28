from odoo import models, fields

class MailTemplate(models.Model):
        _inherit = 'mail.template'

        recipient_type = fields.Char('Recipient Type',
                                     help="Type of the recipient for the email (e.g., 'Customer', 'Internal')")
        save_as_memo = fields.Boolean('Save as Memo', default=False,
                                      help="If checked, the email will be saved as a memo after sending.")
