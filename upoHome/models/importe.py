from odoo import fields,models

class importe(models.Model):
	#Herencia por prototipo
	_inherit = 'upoHome.Gastos'
	_name = 'upoHome.importe'