# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import logging


class Localidad(models.Model):
    _name = 'activos.localidad'

    name = fields.Char("Nombre", required=True)

class Area(models.Model):
    _name = 'activos.area'

    name = fields.Char("Nombre", required=True)
