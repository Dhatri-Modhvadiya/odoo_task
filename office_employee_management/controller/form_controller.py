from odoo import http
from odoo.http import request

class FormController(http.Controller):

    @http.route('/form/website_data', type='http', auth="public", website=True)
    def form_page(self, **kw):
        return request.render('office_employee_management.form_template', {})

    @http.route('/form/submit', type='http', auth="public", website=True, methods=['POST'])
    def form_submit(self, **kw):
        values = {
            'name': kw.get('name'),
            'email': kw.get('email'),
            'user_id': request.env.user.id if request.env.user else None,
        }
        if request.env.user.name == 'Public user':
            request.env['form.data'].sudo().create(values)
        else:
            request.env['private.user'].sudo().create(values)

        return request.redirect('/form/success')

    @http.route('/form/success', type='http', auth="public", website=True)
    def form_success(self, **post):
        return http.request.render("office_employee_management.thankyou_page",{})
        # return "Form submitted successfully!"


