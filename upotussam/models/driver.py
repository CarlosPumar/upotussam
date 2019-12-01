# -*- coding: utf-8 -*-

from odoo import models, fields, api

class driver(models.Model):
    _inherit = 'upotussam.employee'
    _name = 'upotussam.driver'
    carnet = fields.Char('Carnet', size=10, required=True)
    turno = fields.Selection([('morning','Mañana'),
                                     ('afternoon','Tarde'),
                                     ('night','Nocturno')],
                                     'Turno de trabajo')
    autobus_id = fields.Many2one('upotussam.autobus','Autobus')  