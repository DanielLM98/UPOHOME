from typing_extensions import Required
from odoo import models, fields

class Cita(models.Model):
    _name: 'upoHome.Cita'

    id = fields.Float("Identificador de la cita", size=6, required=True)
    hora = fields.Datetime('Hora de la cita', required=True)
    descripcion = fields.Char('Descripcion de la cita',size=60, required=True)