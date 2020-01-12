# -*- coding: utf-8 -*-

from odoo import models, fields, api

class estacion(models.Model):
    _name = 'upotussam.estacion'
    
    nombre = fields.Char('Name', size=64, required=True)
    direccion = fields.Char('Adress', size=64, required=True)
    capacidad = fields.Integer('Capacity')
    plazas_disponibles = fields.Integer('Plazas disponibles')
    autobuses_ids = fields.One2many('upotussam.autobus','estacion_id', 'Autobus') 
    
    #lo suyo seria ponerle un evento a plazas disponibles. AL crear la estacion se pone capacidad 50 pues que le ponga 50 plazas.
    # y cada vez que se "meta" un autobus en la estacion se le reste 1 a las plazas.