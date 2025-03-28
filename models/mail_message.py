from odoo import models, fields, api

class MailMessage(models.Model):
    _inherit = 'mail.message'

    memo_id = fields.Many2one('memo.log', string='Memo')

    @api.model
    def create(self, vals):

        if not vals.get('memo_id'):

            memo = self.env['memo.log'].create({
                'name': 'Memo from message',
                'recipient_type': 'Memo from dd',
                'related_document': 'Memo from message',
                'author_id': self.env.user.id,
            })
            vals['memo_id'] = memo.id


        return super(MailMessage, self).create(vals)
