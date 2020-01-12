# -*- coding: utf-8 -*-

from odoo import models, fields, api


class parada(models.Model):
    _name = 'upotussam.parada'

    nombre = fields.Char('Name', size=64)
    localizacion = fields.Char('Localizacion', size=64)
    estado = fields.Selection([('available', 'Disponible'),
                                     ('unavailable', 'No disponible'),
                                     ('undefined', 'Sin definir'), ],
                                     'Estado de la parada')
    
    linea_ids = fields.Many2many('upotussam.linea', string='Lineas pertenecientes')
    
    #añadir logica algun estado de la parada? para saber si una parada esta accesible o si esta la calle en obras y no se puede contar con ella
    