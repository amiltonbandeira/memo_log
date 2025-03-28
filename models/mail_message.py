from odoo import models, api, fields

class MailMessage(models.Model):
    _inherit = 'mail.message'

    memo_id = fields.Many2one('memo.log', string='Memo')

    @api.model
    def create(self, vals):

        message = super(MailMessage, self).create(vals)
        if not vals('memo_id'):

            memo = self.env['memo.log'].create({
                'name':'Memo for message',
                'recipient_type': 'document',
                'related_document': 'Email',
                'author_id': 'author',
            })

            vals['memo_id'] = memo.id


        return super(MailMessage, self).create(vals)
