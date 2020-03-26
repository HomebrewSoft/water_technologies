# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
#s
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Borrar y editar factura',
    'version': '1.0',
    'author': 'Tinsoft C.B.',
    'category': 'Accounting & Finance',
    'description': """
    Este módulo añade la siguiente funcionalidad a la facturación de Odoo:

    - Permite editar la numeración, fecha, cliente y productos de las facturas, sin necesidad de cancelarlas.
    - Borra facturas incluso en estado validado, tanto dentro de la factura (vista formulario) como en masa (vista árbol).
    - Posibilita el cambio de secuencia de las facturas dentro del menú contabilidad.
====================================


    """,
    'website': 'https://www.tinsoft.es',
    'depends' : ['account','account_cancel'],
    'data': ['borra_facturas_view.xml', 'ir_sequence_view.xml' ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
