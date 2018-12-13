# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleOrder(models.Model):

    _inherit = "sale.order"

    exercice = fields.Text(string='Exercice', translate=True)
