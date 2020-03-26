# -*- coding: utf-8 -*-

from datetime import datetime
import logging
import pytz
import time

import openerp
from openerp.osv import osv
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)

class ir_sequence(openerp.osv.osv.osv):
    inherit = 'ir.sequence'
    _order = 'name'