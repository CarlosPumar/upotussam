# -*- coding: utf-8 -*-
{
    'name': "upotussam",

    'summary': """
        Aplicacion para la gestion de autobuses en un centro urbano""",

    'description': """
        En esta aplicación están recogidos los objetivos
         de gestion de reparaciones y el de gestion de autobuses
    """,

    'author': "grupo 14",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'autobus',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': ['views/reparacionesclass_view.xml'], 

    # only loaded in demonstration mode
    'demo': [
    ],
    
    'application': True,

}