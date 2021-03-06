# -*- coding: utf-8 -*-
{
    'name': 'Facturacion Honduras',
    'version': '1.0',
    'author': 'Ariel Cerrato',
    'description': """
			Nuevo Regimen de facturacion en Honduras. Facturas PreImpresas
    """,
    'depends': ['base', 'account'],
    'data': [
        'views/cai_view.xml',
        'views/ir_sequence_view.xml',
        'views/res_partner_view.xml',
        'views/account_invoice_view.xml',
        'reports/report_sales_receipt.xml',
        "reports/facturas_print.xml",
        "reports/facturas_print2.xml",
        "reports/facturas_print3.xml",   
        "reports/facturas_print_view.xml",
        "reports/facturas_print_view_Preimpresa.xml",
        "reports/facturas_print_view_Preimpresa_Bodega.xml",
    ],
    'update_xml': [
        'security/groups.xml',
        'security/ir.model.access.csv',
    ],
    'installable':True,
}

