# -*- coding: utf-8 -*-

from typing_extensions import Required
from odoo import models, fields

class Alquiler(models.Model):
    _name = 'upohome.Alquiler'
    
    importe = fields.Float("Importe alquiler", size=6, required=True)
    fechaInicio = fields.Datetime('Fecha de inicio', required=True)
    fechaFinal = fields.Datetime('Fecha de finalización', required=True)
    cliente_dni = fields.Many2one('upohome.Cliente','Cliente')
    vivienda_id = fields.Many2one('upohome.Vivienda','Vivienda')
    gastos_id = fields.One2many('upohome.Gastos', 'Gastos')