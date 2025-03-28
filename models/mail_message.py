    from odoo import models, api, fields

    class MailMessage(models.Model):
        _inherit = 'mail.message'

        memo_id = fields.Many2one("memo.log", string='Memo')

        @api.model
        def create_memo_message(self, message_id):
            message = self.browse(message_id)

            memo_vals = {
                'name': message.subject or 'Memo from message',
                'recipient_type': message.body or '',
                'related_document': message.model,
                'author_id': message.author_id.id,
            }

            memo = self.env['memo.log'].create(memo_vals)

            for attachment in message.attachment_ids:
                memo.write({'message_attachment_ids': [(4, attachment.id)]})

            return memo
