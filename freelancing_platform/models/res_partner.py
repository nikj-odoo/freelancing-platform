from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_frelasncer = fields.Boolean('is_frelasncer')
    