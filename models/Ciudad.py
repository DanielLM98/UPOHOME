from typing_extensions import Required
from odoo import models, fields

class Ciudad(model.Model):
    _name="upohome.Ciudad"
    nombre = fields.Char("Nombre de la Ciudad", size=20, required=True)