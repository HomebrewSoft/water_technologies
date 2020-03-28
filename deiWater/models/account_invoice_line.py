# -*- coding: utf-8 -*-
from openerp import api, fields, models


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    isv = fields.Float(
        compute='_get_isv',
    )

    @api.depends('invoice_line_tax_id', 'price_subtotal')
    def _get_isv(self):
        for record in self:
            tax_percentage = sum(record.invoice_line_tax_id.mapped('amount'))
            record.isv = record.price_subtotal - (record.price_subtotal / (1 + tax_percentage))
