# -*- coding: utf-8 -*-
from odoo import http

# class upoHome(http.Controller):
#     @http.route('/upoHome/upoHome/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upoHome/upoHome/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('upoHome.listing', {
#             'root': '/upoHome/upoHome',
#             'objects': http.request.env['upoHome.upoHome'].search([]),
#         })

#     @http.route('/upoHome/upoHome/objects/<model("upoHome.upoHome"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upoHome.object', {
#             'object': obj
#         })
