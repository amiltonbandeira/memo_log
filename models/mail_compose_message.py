from odoo import models, fields

class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    memo_template_id = fields.Many2one('memo.log', string='Memo Template')

    def create_memo_from_template(self):
        if self.memo_template_id:
            memo_vals = {
                'name': self.memo_template_id.name,
                'recipient_type': self.memo_template_id.recipient_type,
                'related_document': self.memo_template_id.related_document,
                'author_id': self.env.user.id,
            }
            memo = self.env['memo.log'].create(memo_vals)
            return memo