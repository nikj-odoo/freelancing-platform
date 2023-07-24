# -*- coding: utf-8 -*-
from odoo import api, fields, models

class FreelancingOfferwizard(models.TransientModel):
    _name = 'fp.offer.wizard'

    # name = fields.Text(string='Name')
    price = fields.Float('Price',required=True,default=0)
    partner_id = fields.Many2one('res.partner',required=True)
    offer_ids = fields.One2many('freelancing.platform.offers','project_id')
    
    # Wizard Button Method
    
    def make_an_offer(self):
        active_ids = self._context.get('active_ids')
        print('------------------------------')
        print(active_ids)
        
        for project_id in active_ids:
            freelancing = self.env['freelaning.platform'].browse(project_id)
            # print(property.mapped('name'))
            
            freelancing.write({
                "offer_ids": [
                    fields.Command.create({
                        "price": self.price,
                        "partner_id": self.partner_id.id,
                    })
                ],
            })
    