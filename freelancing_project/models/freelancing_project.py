# -*- coding: utf-8 -*-
from odoo import models,fields,Command,api


class freelancing_project(models.Model):
    _name = 'freelancing.platform'
    _inherit = ['freelancing.platform']

    @api.model
    def create(self, vals):
        project_name = vals.get('project_name')
        
        project = self.env['project.project'].create({
            'name': project_name,
        })
        
        self.env['project.task'].create(
            {
                'project_id':4,
                'name':'abc'
            }
        )
        return super().create(vals)