from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_freelancer = fields.Boolean('is_freelancer')
    