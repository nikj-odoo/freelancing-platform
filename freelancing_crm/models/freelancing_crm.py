# -*- coding: utf-8 -*-
from odoo import models,fields,Command,api


class freelancing_platform_offers(models.Model):
    _inherit = 'freelancing.platform.offers'

    @api.model
    def create(self, vals):
        # offer_ids = vals.get('offer_ids')
        
        price = vals.get('price')
        partner_id = vals.get('partner_id')
        date_deadline = vals.get('date_deadline')
        print("========================================CRM Called")
        self.env['crm.lead'].sudo().create({
            'stage_id': 1,
            'name':'Quatation For Project',
            'expected_revenue':price,
            'partner_id':partner_id,
            'date_deadline':date_deadline,
            
        })
        return super().create(vals)
