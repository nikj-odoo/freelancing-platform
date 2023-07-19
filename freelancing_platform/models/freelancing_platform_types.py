from odoo import models,fields,api

class freelancing_platform(models.Model):
    _name = "freelancing.platform.types"
    _description = 'This Is Freelancing Platform Types'
    _order = "name"
    
    sequence=fields.Integer("Sequence",default=1)
    project_ids = fields.One2many('freelancing.platform','project_type_id')
    name=fields.Char("Project Type",required=True)
    offer_ids = fields.One2many('freelancing.platform.offers','project_id',string='project type offer')
    offer_count = fields.Integer(compute="_offer_count")
    
    _sql_constraints=[('unique_name','unique(name)','Error! Enter unique name of types')]

    @api.depends("offer_ids")
    def _offer_count(self):
        for i in self:
            i.offer_count = len(i.offer_ids)