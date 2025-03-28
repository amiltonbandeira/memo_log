from odoo import models, api, fields



class MailMessage(models.Model):
    _inherit = 'mail.message'

    memo_id = fields.Many2one("memo.log", 'Memo')

    @api.model
    def create_memo_message(self,vals):
        for message in self:
            memo_vals = {
                'name' : message.name or 'Memo from message '
                'recipient_type' 
                'related_document'
                'create_uid'
                'attachment'
            }
            memo = self.env['memo.log'].create(memo_vals)

