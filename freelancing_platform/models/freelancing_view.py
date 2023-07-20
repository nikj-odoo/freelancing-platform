from psycopg2 import Date
from odoo import models,fields,api, _
from odoo.exceptions import UserError,ValidationError
from  datetime import datetime

class freelancing_platform(models.Model):
    _name = "freelancing.platform"
    _description = 'This Is Freelancing Platform'
    _inherit=['mail.thread','mail.activity.mixin']
    _rec_name="project_name"
    _log_access=False
    _order = "id desc"


    project_name = fields.Char("Project Title", required=True)
    name = fields.Char(string='Number', required=True, copy=False, readonly=False, index=True,default=lambda self:_('New'))

    description = fields.Text("Description")
    partner_id=fields.Many2one("res.partner", string="Company", domain="[('is_company', '=', 'true')]")
    location=fields.Many2one(related="partner_id.state_id", string="Location")
    price=fields.Integer("Price")
    # time_duration=fields.Datetime("Time Duration")
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    duration = fields.Char(string='Duration',compute='compute_date_difference',store=True)
    responsibility=fields.Text("Responsibilty")
    requirements=fields.Text("Requirements")
    experience_level=fields.Selection([('entry',  'Entry Level'),('intermeadiate', 'Intermeadiate Level'),('expert', 'Expert')])
    # job_type =fields.Selection([('office',  'Office'),('remote', 'Remote'),('hybrid', 'Hybrid')])
    proect_type=fields.Selection([('starting',  'Starting'),('ongoing', 'Ongoing'),('maintanance', 'Maintanance')])
    hire_type=fields.Char("Hired Type")
    country=fields.Many2one(related='partner_id.country_id',string="Country")
    sector=fields.Selection([('it',  'IT'),('financial', 'Financial'),('manufacturing', 'Manufacturing'),('e-commerse', 'E-Commerse')])
    project_type_id=fields.Many2one('freelancing.platform.types',string="Project Type")
    skills_ids=fields.Many2many('freelancing.platform.skills',string="Add Skills")
    offer_ids=fields.One2many('freelancing.platform.offers','project_id')
    image = fields.Binary('image')
    offer_ids=fields.One2many('freelancing.platform.offers','project_id', store=True)
    best_offer=fields.Float("Best Offer",compute="_compute_best_offer",store=True)
    state = fields.Selection([('new',  'New'),('offer received', 'Offer Received'),('offer accepted', 'Offer Accepted'),('booked','Booked'),('cancelld','Cancelled ')], 'State',default='new',copy=False,required=True)
    
    _sql_constraints=[('price','CHECK(price >= 0)','A property expected price must be strictly positive.')]
                

    @api.model
    def create(self, vals_list):
        if vals_list.get('name','New') == 'New':
            vals_list['name'] = self.env['ir.sequence'].next_by_code('freelancing.platform.sequence') or 'New'
            return super().create(vals_list)

    @api.depends('start_date', 'end_date')
    def compute_date_difference(self):
        for record in self:
            if record.start_date and record.end_date:
                start = datetime.strptime(str(record.start_date), '%Y-%m-%d')
                end = datetime.strptime(str(record.end_date), '%Y-%m-%d')
                difference = end - start
                record.duration = f"{difference.days} days"
    
    # @api.depends("offer_ids")
    def _compute_best_offer(self):
        if self.offer_ids.price:
            for i in self:
                # print("====================", i.offer_ids)
                i.best_offer =  min(i.offer_ids.filtered(lambda l: l.e_level == 'expert').mapped('price'))
                    

    def action_canceled(self):
            if self.state == 'booked':
                raise UserError("sold property can not be cancelled")
            else:
                self.state = 'cancelld'


    def action_sold(self):
            print("solllddddd")
            if self.state == 'cancelld':
                raise UserError("cancelled property can not be sold")
            else:
                self.state = 'booked'           
        
    @api.ondelete(at_uninstall=False)
    def ondelete(self):
            if self.state != 'new' and self.state != 'cancelld':
                    raise UserError("Only new and canceled properties are deleted")    
                
    @api.depends("offer_ids")
    def _change_state(self):
        for record in self:
            if record.offer_ids:
                record.state="offer received"
