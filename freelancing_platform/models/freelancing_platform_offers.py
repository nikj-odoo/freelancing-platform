from odoo import models,fields,api 
from dateutil.relativedelta import relativedelta
from datetime import datetime
from odoo.exceptions import UserError,ValidationError

from odoo.tools.float_utils import float_compare

class freelancing_platform_offers(models.Model):
    _name = "freelancing.platform.offers"
    _description = 'Projects and Its Offers'
    _order = "price desc"
    
    price = fields.Float(string="Price")
    status = fields.Selection([('A', 'Accepted'),('D', 'Decline')], 'Status',copy=False)
    partner_id=fields.Many2one('res.partner',required=True,domain="[('is_company', '=', 'false')]",string="Freelancer")
    project_id=fields.Many2one('freelancing.platform',required=True)
    property_types_id = fields.Many2one(related="project_id.project_type_id",store=True)
    e_level=fields.Selection([('entry',  'Entry Level'),('intermeadiate', 'Intermeadiate Level'),('expert', 'Expert')])
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline",inverse="_inverse_date_deadline")
    sector=fields.Selection([('it',  'IT'),('financial', 'Financial'),('manufacturing', 'Manufacturing'),('e-commerse', 'E-Commerse')])
    skills_ids=fields.Many2many('freelancing.platform.skills',string="Add Skills")
    
    _sql_constraints = [('check_offer_price','CHECK(price > 0)','A property offer price must be strictly positive.')]
    
            
    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            if type(record.create_date) is not bool:
                record.date_deadline = fields.Date.add(record.create_date, days=record.validity)
            else:
                record.date_deadline = fields.Date.add(fields.Datetime.today(), days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            print("self",self)
            if type(record.create_date) is not bool:
                record.validity = (record.date_deadline - record.create_date.date()).days
            else:
                record.validity = (record.date_deadline - fields.Datetime.today().date()).days
    
    
    @api.model
    def create(self,vals):
        print("=====================================", self)
        if  self.project_id.skills_ids.ids in self.skills_ids.ids:
            raise UserError("Please Enter Required Skills")
        return super().create(vals)
    
    def action_accepted(self):
            for i in self:
                # i.project_id.offer_ids.status == 'D'
                i.status="A"
                if (float_compare(i.price,i.project_id.price * 0.9,precision_rounding=0.01)<0):
                    raise UserError("Selling Price must 90 percent of the expected price")
                else:
                    i.project_id.price = i.price
                    i.project_id.best_offer=i.price
                    i.status = 'A'
                    i.project_id.state='offer accepted'
                    
    def action_decline(self):
            self.status = 'D'
            self.project_id.price = 0
                    
