from typing_extensions import Required
from odoo import models, fields

class Cliente(models.Model):
    dni = fields.Char("DNI del cliente", size=9, require= True)
    nombre = fields.Char("Nombre del cliente", size=30, require=True)
    apellidos = fields.Char("Apellidos del cliente", size=200, require=True)
    telefono = fields.Char("Telefono del cliente", size=9, require=True)
    email = fields.Char("Correo del cliente", size=30, require=False)