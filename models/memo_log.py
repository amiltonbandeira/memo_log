from odoo import models , fields , api

class memo_log(models.Model):
    _name = "memo.log"
    _description = "Memo Log"

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
    body_html = fields.Html(
        'Body', render_engine='qweb', render_options={'post_process': True},
        prefetch=True, translate=True, sanitize='email_outgoing',
    )

    @api.model
    def create(self, vals):
        record = super(memo_log, self).create(vals)

        template = self.env.ref('memo_log.message_user_assigned')
        rendered_html = self.env['ir.qweb'].render(template.id, {'object': record})

        record.body_html = rendered_html

        return record

    @api.model
    def default_get(self, fields):
        res = super(memo_log, self).default_get(fields)

        template = self.env.ref('memo_log.message_user_assigned')
        rendered_html = self.env['ir.qweb']._render(template.id, {'object': self})

        res['body_html'] = rendered_html
        return res


    def action_send_email(self):
        template = self.env.ref('memo_log.email_template_memo_log')

        if template:
            template.send_mail(self.name, force_send=True)
