import json
import werkzeug.wrappers

from odoo import http, _
from odoo.http import request

class PembelianRestApi(http.Controller):
    @http.route(['/api/pembelian_get'], type='http', auth='public', methods=['GET'], csrf=False)
    def pembelian_restapi_get(self, **params):
        pembelian = request.env['pembelian.pembelian'].sudo().search([])
        dict_pembelian = {}
        data_pembelian = []
        for h in pembelian:
            dict_brand = {}
            detail_brand = []
            dict_detail_product = {}
            detail_product = []
            for b in h.brand_ids:
                dict_brand = {'id': b.id, 'name': b.name}
                detail_brand.append(dict_brand)
            for p in h.pembelian_ids:
                dict_detail_product = {'product_id': p.product_id.display_name, 'description': p.description, 'quantity': p.quantity, 'uom_id': p.uom_id.name, 'price': p.price, 'sub_total': p.sub_total}
                detail_product.append(dict_detail_product)
            dict_pembelian = {'id': h.id, 'name': h.name, 'brand_ids': detail_brand, 'pembelian_ids': detail_product}
            data_pembelian.append(dict_pembelian)
        data = {
            'status': 200,
            'message': 'Success',
            'data': data_pembelian
        }
        try:
            return werkzeug.wrappers.Response(
                status=200, 
                content_type='application/json; charset=utf-8',
                headers=[('Access-Control-Allow-Origin', '*')],  # Tambahkan izin CORS di sini
                response=json.dumps(data)
            )
        except:
            return werkzeug.wrappers.Response(
                status=400, 
                content_type='application/json; charset=utf-8',
                headers=[('Access-Control-Allow-Origin', '*')],
                response=json.dumps({
                    'error': 'Error', 
                    'error_description': 'Error Description',
                    })
            )
