from odoo import fields,models

class Descripcion(models.Model):
	#Herencia por prototipo
	_inherit = 'upoHome.Gastos'
	_name = 'upoHome.Descripcion'