# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import logging


class Etiquetas(models.Model):
    _name = 'activos.localidad.etiqueta'

    name = fields.Char("Nombre", required=True)

class Localidad(models.Model):
    _name = 'activos.localidad'

    name = fields.Char("Nombre", required=True)
    etiqueta_ids = fields.Many2many('activos.localidad.etiqueta', 'localidad_etiqueta_rel', 'localidad_id', 'etiqueta_id', string='Etiquetas')

