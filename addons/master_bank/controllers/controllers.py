# -*- coding: utf-8 -*-
# from odoo import http


# class MasterBank(http.Controller):
#     @http.route('/master_bank/master_bank', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/master_bank/master_bank/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('master_bank.listing', {
#             'root': '/master_bank/master_bank',
#             'objects': http.request.env['master_bank.master_bank'].search([]),
#         })

#     @http.route('/master_bank/master_bank/objects/<model("master_bank.master_bank"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('master_bank.object', {
#             'object': obj
#         })

