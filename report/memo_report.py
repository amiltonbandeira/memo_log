from odoo import api, models

class MemoReport(models.AbstractModel):
    _name = 'report.memo_log.memo_report_document'

    def _get_report_values(self, docids, data=None):
        docs = self.env['memo.log'].browse(docids)
        return {
            'docs': docs,
        }
