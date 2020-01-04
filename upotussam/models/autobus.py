# -*- coding: utf-8 -*-

from odoo import models, fields, api


class autobus(models.Model):
    _name = 'upotussam.autobus'

    matricula = fields.Char('Matrícula', size=64, required=True)
    capacidad = fields.Integer("Capacidad") 
    estado = fields.Selection([('available', 'Disponible'),
                                     ('active', 'Activo'),
                                     ('repair', 'En reparación'), ],
                                     'Estado del autobús')
    driver_id =  fields.Many2one('upotussam.driver','Conductor')  
    reparacion_id = fields.Many2one('upotussam.reparacion','Reparacion')  