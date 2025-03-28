from odoo import models, api, fields

class MailMessage(models.Model):
    _inherit = 'mail.message'

    memo_id = fields.Many2one('memo.log', string='Memo')

    @api.model
    def create(self, vals):

        message = super(MailMessage, self).create(vals)

        self.create_memo(message)
        return message

    def create_memo(self,message):

        if not message.memo_id:

            memo_vals = self.env['memo.log'].create({
                'name':'Memo for message',
                'recipient_type': 'document',
                'related_document': 'Email',
                'author_id': 'author',
            })

            memo = self.env['memo.log'].create(memo_vals)

            message.memo_id = memo.id

        return message.memo_id
