from odoo import models, api, fields



class MailMessage(models.Model):
    _inherit = 'mail.message'

    memo_id = fields.Many2one("memo.log", 'Memo')

    @api.model
    def create(self, vals):
        pass
