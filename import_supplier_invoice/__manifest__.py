# -*- coding: utf-8 -*-
{
    'name': 'Import Supplier Invoice',
    'category': '',
    'summary': 'Import supplier invoices',
    'description': "Module to import supplier invoices",
    'version': '1.0',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'wizard/import_supplier_invoice.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
