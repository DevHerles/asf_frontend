# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class CondominiumFrontend(http.Controller):

    @http.route('/page/schedule', auth='public', website=True)
    def list(self, **kw):
        return http.request.render('website.features')

    @http.route('/page/dashboard', auth='public', website=True)
    def dashboard(self, **kw):
        users = http.request.env['res.users']
        vals = {'title': 'Employees', 'users': users.search([])}
        return http.request.render('website.dashboard', vals)

    @http.route('/dashboard/data', type="json", auth='user', website=True)
    def fetch_dashboard_data(self, **kw):
        cr, context, pool, uid = request.cr, request.context, request.registry, request.uid
        input_data = kw.get('input_data')

        params = request.env['ir.config_parameter']
        ga_client_id = params.sudo().get_param('google_management_client_id', default='')

        return {
            'user': {'user_id': request.env.user.name},
            'currency': request.env.user.company_id.currency_id.id,
            'dashboards': {
                'visits': {
                    'ga_client_id': ga_client_id,
                }
            }
        }

    @http.route('/page/features', auth='public', website=True)
    def list(self, **kw):
        return http.request.render('website.features')

    @http.route('/page/pricing', auth='public', website=True)
    def list(self, **kw):
        return http.request.render('website.pricing')

    @http.route('/page/sendemail', type='http', auth="public")
    def send_email(self, redirect=None, **kw):
        me = 'noreply@duplex.pe'
        to = 'herles.incalla@gmail.com'

        if http.request.httprequest.method == 'POST':
            name = http.request.params['name']
            email = http.request.params['email']
            phone = http.request.params['phone']
            website = http.request.params['website']
            message = http.request.params['message']
            print (email);

            msg = MIMEMultipart('alternative')
            msg['Subject'] = 'Contact Us'
            msg['From'] = 'noreply@duplex.pe'
            msg['To'] = me

            text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
            html = """\
            <html>
            <head></head>
            <body>
                <p>Hi!<br>
                How are you?<br>
                Here is the <a href="https://www.python.org">link</a> you wanted.
                </p>
            </body>
            </html>
            """

            # Record the MIME types of both parts - text/plain and text/html.
            part1 = MIMEText(text, 'plain')
            part2 = MIMEText(html, 'html')

            # Attach parts into message container.
            # According to RFC 2046, the last part of a multipart message, in this case
            # the HTML message, is best and preferred.
            msg.attach(part1)
            msg.attach(part2)

            # Send the message via local SMTP server.
            s = smtplib.SMTP('localhost')
            # sendmail function takes 3 arguments: sender's address, recipient's address
            # and message to send - here it is sent as one string.
            s.sendmail(me, to, msg.as_string())
            s.quit()

        return http.request.render('website.pricing')

#     @http.route('/duplex_fe/duplex_fe/objects/<model("duplex_fe.duplex_fe"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('duplex_fe.object', {
#             'object': obj
#         })