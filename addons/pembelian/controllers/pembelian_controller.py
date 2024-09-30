import json
from odoo import http
from odoo.http import request

class PembelianRestApi(http.Controller):
    @http.route(['/api/pembelian_get'], type='http', auth='public', methods=['GET'], csrf=False)
    def pembelian_restapi_get(self, **params):
        pembelian = request.env['pembelian.pembelian'].sudo().search([])
        data_pembelian = []

        for h in pembelian:
            detail_brand = []
            detail_product = []

            for b in h.brand_ids:
                detail_brand.append({'id': b.id, 'name': b.name})

            for p in h.pembelian_ids:
                detail_product.append({
                    'product_id': p.product_id.display_name,
                    'description': p.description,
                    'quantity': p.quantity,
                    'uom_id': p.uom_id.name,
                    'price': p.price,
                    'sub_total': p.sub_total,
                })

            dict_pembelian = {
                'id': h.id,
                'name': h.name,
                'brand_ids': detail_brand,
                'pembelian_ids': detail_product,
            }
            data_pembelian.append(dict_pembelian)

        data = {
            'status': 200,
            'message': 'Success',
            'data': data_pembelian
        }

        try:
            return request.make_response(
                json.dumps(data),
                headers=[('Content-Type', 'application/json; charset=utf-8'), ('Access-Control-Allow-Origin', '*')],
            )
        except Exception as e:
            return request.make_response(
                json.dumps({
                    'error': 'Error',
                    'error_description': str(e),
                }),
                status=400,
                headers=[('Content-Type', 'application/json; charset=utf-8'), ('Access-Control-Allow-Origin', '*')],
            )
