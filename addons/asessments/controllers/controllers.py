# -*- coding: utf-8 -*-
# from odoo import http


# class Asessments(http.Controller):
#     @http.route('/asessments/asessments', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asessments/asessments/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('asessments.listing', {
#             'root': '/asessments/asessments',
#             'objects': http.request.env['asessments.asessments'].search([]),
#         })

#     @http.route('/asessments/asessments/objects/<model("asessments.asessments"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asessments.object', {
#             'object': obj
#         })

