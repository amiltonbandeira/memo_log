from odoo import models, fields

class MailTemplate(models.Model):
    _inherit = 'mail.template'

    recipient_type = fields.Char('Recipient Type',
                                 help="Type of the recipient for the email (e.g., 'Customer', 'Internal')")
    save_as_memo = fields.Boolean('Save as Memo', default=False,
                                  help="If checked, the email will be saved as a memo after sending.")

    def send_mail(self, template_id, model_id=None, res_id=None, force_send=False, email_values=None):

        result = super(MailTemplate, self).send_mail(template_id, model_id, res_id, force_send, email_values)

        if self.save_as_memo:
            record = self.env[model_id].browse(res_id)

            self.create_memo(record)

        return result

    def create_memo(self, record):

        memo_vals = {
            'name': 'Memo for message',
            'recipient_type': 'document',
            'related_document': 'Email',
            'author_id': 'author',
        }
        memo = self.env['memo.log'].create(memo_vals)

        if hasattr(record, 'memo_ids'):
            record.memo_ids = [(4, memo.id)]

        return memo
