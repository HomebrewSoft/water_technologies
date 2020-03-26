from openerp import models, fields, api
from openerp.exceptions import except_orm, Warning, RedirectWarning
import logging

_logger = logging.getLogger(__name__)

class account_invoice(models.Model):
	_inherit = ['account.invoice']

	@api.one
	def unlink(self):
		#raise Warning('ERROR')
		'''for invoice in self:
			if invoice.state not in ('draft', 'cancel'):
				raise Warning('asdwwwss')'''
		_logger.info('Borrada factura con id = %s', self.id)

		return models.Model.unlink(self)