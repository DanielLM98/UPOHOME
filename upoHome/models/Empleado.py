# -*- coding: utf-8 -*-

from typing_extensions import Required
from odoo import fields, models


class empleado(models.Model):
    _name = 'upoHome.Empleado'
    
    name = fields.Char('DNI del empleado', size=9, required=True)
    nombre = fields.Char('Nombre del empleado', size=30, required=True)
    apellidos = fields.Char('Apellidos del empleado', size=200, required=True) 
    telefono = fields.Char('Telefono del empleado', size=9, required=True)
    email = fields.Char("Email del empleado",size=30, required=False)
    