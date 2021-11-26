# -*- coding: utf-8 -*-

from typing_extensions import Required
from odoo import models, fields

class Direccion(models.Model):
	calle = fields.Char('Calle de la vivienda',size=60, required=True)
    numero = fields.Char("Nombre del cliente", size=30, require=True)