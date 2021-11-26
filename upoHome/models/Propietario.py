from typing_extensions import Required
from odoo import models, fields

class Propietario(models.Model):
    dni = fields.Char("DNI del propietario", size=9, require= True)
    nombre = fields.Char("Nombre del propietario", size=30, require=True)
    apellidos = fields.Char("Apellidos del propietario", size=200, require=True)
    telefono = fields.Char("Telefono del propietario", size=9, require=True)
    email = fields.Char("Correo del propietario", size=30, require=False)