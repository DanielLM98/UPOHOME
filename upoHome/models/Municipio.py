# -*- coding: utf-8 -*-

from typing_extensions import Required
from odoo import models, fields

class Municipio(models.Model):
	_name = 'upoHome.Municipio'

	nombre = fields.Char('Nombre del municipio',size=60, required=True)
    cp = fields.Float("Codigo postal",size=10, required=True)