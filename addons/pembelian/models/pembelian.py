from odoo import models, fields

class Pembelian(models.Model):
    _name = 'pembelian.pembelian'

    name = fields.Char(string='Name')
    tanggal = fields.Date(string='Tanggal')
    status = fields.Selection([('draft', 'Draft'), ('to_approve', 'To Approve'), ('approved', 'Approved'), ('done', 'Done')])
