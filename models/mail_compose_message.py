from odoo import models, fields, api

class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    memo_template_id = fields.Many2one('memo.log', string='Memo Template')

    def create_memo_from_template(self):

        if self.memo_template_id:

            memo_vals = {
                'name': 'Memo from message',
                'recipient_type': 'Memo from dd',
                'related_document': 'Memo from message',
                'author_id': self.env.user.id,
            }

            memo = self.env['memo.log'].create(memo_vals)

            return memo
        else:
            return None
