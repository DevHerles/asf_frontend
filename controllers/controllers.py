# -*- coding: utf-8 -*-
from odoo import http

class CondominiumFrontend(http.Controller):
    # @http.route('/page/duplex_fe/', auth='public', website=True)
    # def index(self, **kw):
    #     # return "Hello, world 222"
    #     Teachers = http.request.env['duplex_fe.teachers']

    #     return http.request.render('duplex_fe.index', {
    #         'teachers': Teachers.search([]),
    #     })

    @http.route('/page/features', auth='public', website=True)
    def list(self, **kw):
        return http.request.render('website.features')

    @http.route('/page/pricing', auth='public', website=True)
    def list(self, **kw):
        return http.request.render('website.pricing')

#     @http.route('/duplex_fe/duplex_fe/objects/<model("duplex_fe.duplex_fe"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('duplex_fe.object', {
#             'object': obj
#         })