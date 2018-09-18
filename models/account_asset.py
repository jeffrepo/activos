# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountAssetAsset(models.Model):
    _inherit = 'account.asset.asset'

    ubicacion_id = fields.Many2one('stock.location', string='Ubicacion')
    responsable_id = fields.Many2one('hr.employee', string='Responsable')
    numero_de_serie = fields.Char('Numero de serie')
    marca = fields.Char('Marca')
    modelo = fields.Char('Modelo')
    etiqueta = fields.Char('Etiqueta')
    estado = fields.Selection([
        ('bueno', 'Bueno'),
        ('regular', 'Regular'),
        ('malo', 'Malo'),
    ])



