# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleOrder(models.Model):

    _inherit = "sale.order"

    # Ajouter un champ texte nommé « Exercice »
    # Ajouter une traduction en anglais et français
    # Tout ajout supplémentaire (champ calculé, relation…) qui démontrera une recherche approfondie sera apprécié