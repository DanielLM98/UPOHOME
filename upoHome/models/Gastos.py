# -*- coding: utf-8 -*-

from odoo import fields,models


class Gastos(models.Model):
    _name = 'upohome.Gastos'
    
    name = fields.Integer('Id de gastos', size=6, required=True)
    importe = fields.Float("Importe del gasto", required = True)
    descripcion = fields.Char("Descripcion del gasto",size=60,required = True)
    tipo = fields.Selection([('agua', 'Agua'),
                              ('internet', 'Internet'),
							  	('electricidad', 'Electricidad'),  
								  ('gas', 'Gas'),],
                              		"Tipo de gasto contratado", required=True)

    alquiler_id = fields.Many2one('upoHome.alquiler', 'Alquiler')
    _sql_constraints = [('upoHome_Gastos_name_unique','UNIQUE (name)','El número de Gastos debe ser único')]
