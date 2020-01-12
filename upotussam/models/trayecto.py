# -*- coding: utf-8 -*-

from odoo import models, fields, api


class trayecto(models.Model):
    _name = 'upotussam.trayecto'

    dias = fields.Selection([('1', 'L-X-V'),
                                     ('2', 'M-J'),
                                     ('3', 'V-S-D'),
                                     ('4', 'Todos'), ],
                                     'Dias de trayecto')
    hora_salida = fields.Float('Hora salida')
    hora_llegada = fields.Float('Hora llegada')

    autobus_id =  fields.Many2one('upotussam.autobus','Autobus')
    linea_id = fields.Many2one('upotussam.linea','Linea')