from odoo import models,fields

class freelancing_platform_skills(models.Model):
    _name = "freelancing.platform.skills"
    _description = 'This Is Freelancing Platform'
    _order = "name"


    name = fields.Char("Skills", required=True)
    color = fields.Integer('color')
    # offer_ids=fields.One2many('freelancing.platform.offers','skills_ids')
    
    _sql_constraints=[('unique_name','unique(name)','Error! Enter unique name of Skiils')]