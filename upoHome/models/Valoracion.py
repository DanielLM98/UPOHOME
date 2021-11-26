# -*- coding: utf-8 -*-

from typing_extensions import Required
from odoo import models, fields

class Valoracion(models.Model):
	puntuacion = fields.int("Puntuacion",size=2, required=True)
    descripcion = fields.Char("Nombre del cliente", size=30, require=True)