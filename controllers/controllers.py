# -*- coding: utf-8 -*-
from odoo import http

class CondominiumFrontend(http.Controller):
    @http.route('/page/condominium_frontend/', auth='public', website=True)
    def index(self, **kw):
        # return "Hello, world 222"
        Teachers = http.request.env['condominium_frontend.teachers']

        return http.request.render('condominium_frontend.index', {
            'teachers': Teachers.search([]),
        })

#     @http.route('/condominium_frontend/condominium_frontend/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('condominium_frontend.listing', {
#             'root': '/condominium_frontend/condominium_frontend',
#             'objects': http.request.env['condominium_frontend.condominium_frontend'].search([]),
#         })

#     @http.route('/condominium_frontend/condominium_frontend/objects/<model("condominium_frontend.condominium_frontend"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('condominium_frontend.object', {
#             'object': obj
#         })