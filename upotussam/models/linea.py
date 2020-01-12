# -*- coding: utf-8 -*-

from odoo import models, fields, api


class linea(models.Model):
    _name = 'upotussam.linea'

    nombre = fields.Char('Name', size=64)
    capacidad = fields.Integer("Capacidad") 
    afluencia = fields.Selection([('high', 'Alta'),
                                     ('low', 'Baja'),
                                     ('medium', 'Media'), ],
                                     'Afluencia de la parada')
    trayecto_id =  fields.Many2one('upotussam.trayecto','Trayecto')
    parada_ids = fields.Many2many('upotussam.parada', string='Paradas asignadas')