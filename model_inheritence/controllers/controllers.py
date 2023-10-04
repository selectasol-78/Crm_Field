# -*- coding: utf-8 -*-
# from odoo import http


# class ModelInheritence(http.Controller):
#     @http.route('/model_inheritence/model_inheritence', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/model_inheritence/model_inheritence/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('model_inheritence.listing', {
#             'root': '/model_inheritence/model_inheritence',
#             'objects': http.request.env['model_inheritence.model_inheritence'].search([]),
#         })

#     @http.route('/model_inheritence/model_inheritence/objects/<model("model_inheritence.model_inheritence"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('model_inheritence.object', {
#             'object': obj
#         })
