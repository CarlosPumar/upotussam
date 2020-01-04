# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mecanico(models.Model):
    _inherit = 'upotussam.employee'
    _name = 'upotussam.mecanico'
    especialidad = fields.Char('Especialidad', size=20, required=True)
    centroDocente = fields.Char('Centro de Estudios', size=20, required=False)
    
    taller_id = fields.Many2one('upotussam.taller', 'Taller')
    reparacion_ids = fields.Many2many('upotussam.reparacion', string='Reparaciones involucrado/a')
    