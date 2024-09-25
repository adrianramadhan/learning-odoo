from odoo import models, fields, api

class Pembelian(models.Model):
    _name = 'pembelian.pembelian'

    name = fields.Char(string='Name')
    tanggal = fields.Date(string='Tanggal')
    status = fields.Selection([('draft', 'Draft'), ('to_approve', 'To Approve'), ('approved', 'Approved'), ('done', 'Done')], default='draft', string='Status')
    pembelian_ids = fields.One2many('pembelian.line', 'pembelian_id', string='Pembelian Ids')
    brand_ids = fields.Many2many('pembelian.brand', 'pembelian_brand_rel', 'pembelian_id', 'brand_id', string='Brand Ids')

class pembelian_line(models.Model):
    _name = 'pembelian.line'

    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id:
            self.description = self.product_id.name
        return {}

    pembelian_id = fields.Many2one('pembelian.pembelian', string='Pembelian ID')
    product_id = fields.Many2one('product.product', string='Product')
    description = fields.Text(string='Description')
    quantity = fields.Float(string='Quantity', default=0.0)
    uom_id = fields.Many2one('uom.uom', string='Uom Id')

class Brand(models.Model):
    _name = 'pembelian.brand'

    name = fields.Char(string='Name')