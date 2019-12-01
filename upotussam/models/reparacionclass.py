from odoo import models, fields, api


class reparacionesclass(models.Model):
    _name = 'upotussam.reparacionesclass'
    descripcion = fields.Char('Descripcion', size=64, required=True)
    fechaInicio = fields.Datetime('Fecha de Inicio', required=True, autodate=True)
    fechaFin = fields.Datetime('Fecha de Fin', required=True, autodate=True)
    garantia = fields.Integer("Años de Garantia")
    autobus_id = fields.Many2one('upotussam.autobus','Autobus')  