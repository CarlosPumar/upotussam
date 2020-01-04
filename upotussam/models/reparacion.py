from odoo import models, fields, api
from _cffi_backend import string


class reparacion(models.Model):
    _name = 'upotussam.reparacion'
    descripcion = fields.Char('Descripcion', size=64, required=True)
    fechaInicio = fields.Datetime('Fecha de Inicio', required=True, autodate=True)
    fechaFin = fields.Datetime('Fecha de Fin', required=True, autodate=False)
    garantia = fields.Integer("Años de Garantia")
    
    autobus_id = fields.Many2one('upotussam.autobus','Autobus')  
    piezas_ids = fields.Many2many('upotussam.piezas', string='Piezas')
    mecanico_ids = fields.Many2many('upotussam.mecanico', string='Mecanicos involucrados')