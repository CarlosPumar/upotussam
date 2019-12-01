# -*- coding: utf-8 -*-

from odoo import models, fields, api

class employee(models.Model):
    _name = 'upotussam.employee'
    dni = fields.Char('DNI', size=9, required=True)
    nombre = fields.Char('Name', size=64, required=True)
    apellidos = fields.Char('Surnames', size=64, required=True)
    mail = fields.Char('Mail', size=64, required=False)
    fecha_nacimiento = fields.Date('Birthdate', autodate = True)
    tipo_contrato = fields.Selection([('full-time','Completo'),
                                     ('part-time','Parcial'),],
                                     'Type of contract')