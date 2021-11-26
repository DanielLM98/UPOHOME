# -*- coding: utf-8 -*-

from typing_extensions import Required
from odoo import models, fields

class TipoGasto(models.Model):
	#Herencia por prototipo
	_inherit = 'upoHome.Gastos'
	_name = 'upoHome.TipoGasto'
  
  	