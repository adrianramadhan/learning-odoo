from odoo import models, fields, api

class Pembelian(models.Model):
    _name = 'pembelian.pembelian'

    def action_to_approve(self):
        if self.status == 'draft':
            if self.name == 'New':
                seq = self.env['ir.sequence'].next_by_code('pembelian.pembelian') or 'New'
                self.name = seq
            self.status = 'to_approve'

    def action_approved(self):
        if self.status == 'to_approve':
            self.status = 'approved'
    
    def action_done(self):
        if self.status == 'approved':
            self.status = 'done'

    name = fields.Char(string='Name', default='New')
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
    
    @api.depends('quantity', 'price')
    def _amount_total(self):
        for rec in self:
            rec.sub_total = rec.quantity * rec.price

    # def _domain_product_id(self):
    #     product_obj = self.env['product.product'].search([('type', '=', 'product')])
    #     domain = [('id', 'in', product_obj.ids)]
    #     return domain

    pembelian_id = fields.Many2one('pembelian.pembelian', string='Pembelian ID')
    product_id = fields.Many2one('product.product', string='Product Id')
    description = fields.Text(string='Description')
    quantity = fields.Float(string='Quantity', default=0.0)
    price = fields.Float(string='Price', default=0.0)
    sub_total = fields.Float(string='Sub Total', compute=_amount_total, store=True)
    uom_id = fields.Many2one('uom.uom', string='Uom Id')

class Brand(models.Model):
    _name = 'pembelian.brand'

    name = fields.Char(string='Name')