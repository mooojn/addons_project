from odoo import http
from odoo.http import request

class TaskLyft(http.Controller):

    @http.route(['/services'], type='http', auth='public', website=True)
    def services_page(self, **kwargs):
        domain = []

        # Get filter parameters
        category = kwargs.get('category')
        title = kwargs.get('title')
        experience_level = kwargs.get('experience_level')
        price_range = kwargs.get('price_range')

        # Apply category filter
        if category:
            domain.append(('category', '=', category))

        # Apply title filter
        if title:
            domain.append(('title', 'ilike', title))

        # Apply experience level filter
        if experience_level:
            domain.append(('experience_level', '=', experience_level))

        # Apply price range filter
        if price_range:
            price_min, price_max = price_range.split('-')
            if price_min:
                domain.append(('price_per_hour', '>=', float(price_min)))
            if price_max:
                domain.append(('price_per_hour', '<=', float(price_max)))

        # Fetch filtered services
        services = request.env['tasklyft.service'].sudo().search(domain)

        return request.render('task_lyft.services_page', {
            'services': services
        })
