# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.modules import module
from odoo.exceptions import UserError, ValidationError
import base64
import os
import pandas

class ImportSupplierInvoice(models.TransientModel):
    _name = 'import.supplier.invoice'

    excel = fields.Binary('Excel file (recommended format: xlsx) to import')

    def importar(self):
        excel = self.excel
        path = os.path.join(module.get_module_path('import_supplier_invoice'), 'tmp', 'cc.xlsx')
        fileobj = open(path, "wb")
        if excel != False:
            fileobj.write(base64.b64decode(excel))
            fileobj.flush()
            fileobj.close()
        else:
            raise UserError(_('Select an excel file!!'))

        datos = pandas.read_excel(path)
        cant_filas = datos.shape[0]
        obj_account_move = self.env['account.move']
        for i in range(cant_filas):
            partner_id = self.env['res.partner'].search([('name','=',datos.values[i][4])])
            producto_id = self.env['product.product'].search([('name', '=', datos.values[i][6])])
            record_account_move = obj_account_move.create({
                'invoice_date':datos.values[i][0],
                # 'amount_total':datos.values[i][3],
                'partner_id':partner_id.id,
                'name':datos.values[i][5],
                'move_type': 'in_invoice',
                # 'line_ids':[(0, 0, {'product_id':producto_id.id, 'quantity':1, 'price_unit':producto_id.standard_price})],
                'state': 'draft'
            })

