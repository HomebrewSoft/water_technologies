# -*- coding: utf-8 -*-
#
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2016 Clear ICT Solutions (<info@clearict.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

from openerp import api, models


class PurgeWizard(models.TransientModel):

    """ Main wizard for cleaning up model content """

    _inherit = 'cleanup.content.wizard'

    @api.model
    def get_model_list(self):
        """
        Returns a list of models whose content should be removed.
        """

        res = super(PurgeWizard, self).get_model_list()
        res += [
            'account.analytic.line',
            'account.bank.statement',
            'account.bank.statement.line',
            'account.cashbox.line',
            'account.invoice',
            'account.invoice.line',
            'account.invoice.tax',
            'account.move',
            'account.move.line',
            'account.move.reconcile',
            'account.subscription',
            'account.subscription.line',
        ]

        return res

    @api.model
    def get_extra_tables_list(self):
        """
        Returns a list of dictionaries containing additional database table
        names to reset for each model:
            { 'model.name': ['extra_table1', 'extra_table2'] }
        """

        res = super(PurgeWizard, self).get_extra_tables_list()
        res += [
            {
                'account.invoice.line': [
                    'account_invoice_line_tax',
                    'purchase_order_line_invoice_rel',
                ],
                'account.move.line': ['account_move_line_relation'],
            },
        ]

        return res
