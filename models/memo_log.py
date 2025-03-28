from odoo import models , fields , api

class memo_log(models.Model):
    _name = 'memo.log'
    _description = 'Memo log model'
    _inherit = ['mail.thread' , 'mail.activity.mixin']

    name = fields.Char(string="Title", required=True)
    recipient_type = fields.Char(string = "Recipient Type")
    related_document = fields.Char(string = "Related Document ")
    attachment = fields.Boolean("Attachment")
    patient_id = fields.Many2one("res.partner", string="Patient" )
    project_id = fields.Many2one("project.task" , string="Project Id")
    message_ids = fields.One2many('mail.message', 'res_id', domain=[('model', '=', 'memo.log')], string="Messages")
    message_attachment_ids = fields.Many2many('ir.attachment', string="Attachments")
    author_id = fields.Many2one("res.users", string="From", default=lambda self: self.env.user)
    partner_ids = fields.Many2many("res.partner", "memo_log_partner" , "memo_id" , "partner_id" , string="To (partners)")
    cc_partner_ids = fields.Many2many("res.partner","memo_log_cc_partner", "memo_id", "partner_id", string="CC")





