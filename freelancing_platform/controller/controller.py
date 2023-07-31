from odoo import http,fields
from odoo.http import request
from dateutil.relativedelta import relativedelta
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager

class Freelancing(http.Controller):

    @http.route(['/freelancing', '/freelancing/page/<int:page>'], auth='public',website=True)
    def index(self,page=0, **kw):
        domain=[]
        
        #domain = [('state','in',['new','offer received','offer accepted'])]
        total = http.request.env['freelancing.platform'].sudo().search_count([])
        
                
        _items_per_page = 6
        pager = portal_pager(
            url="/freelancing",
            total=total,
            page=page,
            step=_items_per_page
        )
        
        Teachers = http.request.env['freelancing.platform'].search(domain)
        return http.request.render('freelancing_platform.index',{
            'teachers': Teachers.search(domain,limit=_items_per_page, offset=pager['offset'],order='id asc'),'pager':pager
        })


    @http.route('/freelancing_platform/<model("freelancing.platform"):freelancing>/', auth='public', website=True)
    def teacher(self, freelancing):
        return http.request.render('freelancing_platform.description', {
        'freelancing': freelancing
        })



