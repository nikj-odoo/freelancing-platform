# -*- coding: utf-8 -*-
from odoo import models,fields,Command


class freelancing_account(models.Model):
    _name = 'freelancing.platform'
    _inherit = 'freelancing.platform'
    


    def action_sold(self):
        print("account method is called")
        self.env['account.move'].create(
            {
                'move_type':'out_invoice',
                
                'invoice_date':fields.Date.context_today(self),
                'invoice_line_ids':[
                    Command.create({
                        'name':self.project_name,
                        'price_unit':self.price,
                        'quantity':1,
                        'tax_ids':[1]
                    }),

                    Command.create({
                        'name':self.project_name,
                        'price_unit':100,
                        'quantity':1,
                        'tax_ids':[1]
                    })
                ]

        }
        )
        
        return super().action_sold()
