from odoo import models, api, fields



class MailMessage(models.Model):
    _inherit = 'mail.message'

    memo_id = fields.Many2one("memo.log", 'Memo')

    @api.model
    def create_memo_message(self,message_id):
            message = self.browse(message_id)
            memo_vals = {
                'name' : message.name or 'Memo from message ',
                'recipient_type' : message.body or '',
                'create_uid' : self.env.uid,
            }

            memo = self.env['memo.log'].create(memo_vals)


                for attachment in message.attachment_ids:
                    memo.write({'attachment_ids': [(4, attachment.id)]})

                return memo