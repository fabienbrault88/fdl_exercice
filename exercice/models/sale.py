# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleOrder(models.Model):

    _inherit = "sale.order"

    @api.one
    @api.depends("exercice")
    def get_compute_exercice(self) :
    	self.compute_exercice = "compute " + self.exercice

    exercice = fields.Text(string='Exercice', translate=True)

    compute_exercice = fields.Text(string="Compute Exercice", compute="get_compute_exercice")

    relation_exercice = fields.Many2one('res.partner', string="Relation Exercice")
