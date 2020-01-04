# -*- coding: utf-8 -*-

from odoo import models, fields, api


class piezas(models.Model):
    _name = 'upotussam.piezas'

    nombre = fields.Char('Nombre', size=64, required=True)
    precio = fields.Integer('Precio')
    segundaMano = fields.Selection([('yes', 'Si'),
                                    ('no', 'No'),],
                                   'Segunda Mano')
    
    reparaciones_ids = fields.Many2many('upotussam.reparacion', string='Reparaciones')