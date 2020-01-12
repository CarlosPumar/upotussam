# -*- coding: utf-8 -*-

from odoo import models, fields, api


class taller(models.Model):
    _name = 'upotussam.taller'

    direccion = fields.Char('Taller de Reparacion', size=20, required=True)
    telefono = fields.Char('Telefono', size=9, required=True)
    correoElectronico = fields.Char('Correo Electronico', size=20, required=True)
    mecanicos_ids = fields.One2many('upotussam.mecanico','taller_id', 'Mecanico') 
