from odoo import models, api, fields
from odoo.exceptions import ValidationError

class MailMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    memo_id = fields.Many2one('memo.log', string='Memo')

    @api.model
    def create(self, vals):

        if not vals('memo_id'):
            memo = self.env['memo.log'].create({
                'name': 'Memo for message ',
                'recipient_type': 'Email',
                'related_document': 'document',
                'author_id': 'author',
            })
            vals['memo_id'] = memo.id

        return super(MailMessage, self).create(vals)
