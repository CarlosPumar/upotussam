from odoo import models, fields, api
from _cffi_backend import string


class reparacion(models.Model):
    _name = 'upotussam.reparacion'
    descripcion = fields.Char('Descripcion', size=64, required=True)
    fechaInicio = fields.Datetime('Fecha de Inicio', required=True, autodate=True)
    fechaFin = fields.Datetime('Fecha de Fin', required=True, autodate=True)
    mensajeCancelacion = fields.Char('Mensaje de Cancelacion', size=64, required=False)
        
    autobus_id = fields.Many2one('upotussam.autobus','Autobus', required=True)  
    piezas_ids = fields.Many2many('upotussam.piezas', string='Piezas')
    mecanico_ids = fields.Many2many('upotussam.mecanico', string='Mecanicos involucrados')
    
    state = fields.Selection([('espera','En espera'),
                              ('enviado','Autobus enviado'),
                              ('reparacion','En reparacion'),
                              ('finalizado','Finalizado'),
                              ('cancelado','Cancelado'),],
                              'Estado',
                              default='espera')
    
    #botones
    
    @api.one
    def btn_submit_to_enviado(self):
        self.write({'state':'enviado'})
    
    @api.one
    def btn_submit_to_reparacion(self):
        if not self.mecanico_ids:
            raise models.ValidationError('Se tiene que asignar un mecanico minimo')
        else:
            self.write({'state':'reparacion'})
        
    @api.one
    def btn_submit_to_finalizado(self):
            self.write({'state':'finalizado'})
            
    @api.one
    def btn_submit_to_cancelado(self):
        self.write({'state':'cancelado'})
        
        
    #onchanges
    
    @api.onchange('piezas_ids')
    def onchange_piezas(self):
        if self.state != 'enviado':
            raise models.ValidationError('Solo se pueden asignar las piezas cuando se haya enviado el autobus a reparar')
        
    @api.onchange('mecanico_ids')
    def onchange_mecanico(self):
        if self.state != 'enviado':
            raise models.ValidationError('Solo se pueden asignar los mecanicos cuando se haya enviado el autobus a reparar')
        
    @api.onchange('descripcion', 'fechaInicio', 'fechaFin', 'garantia', 'autobus_id', 'piezas_ids', 'mecanico_ids')
    def onechange_cancelar(self):
        if self.state == 'cancelado':
            raise models.ValidationError('Una vez cancelado no se puede modificar')
        
    @api.onchange('mensajeCancelacion')
    def onchange_mecanico(self):
        if self.state != 'cancelado':
            raise models.ValidationError('Solo se puede añadir un mensaje si la reparacion se ha cancelado')
        
    @api.multi
    @api.onchange('mecanico_ids')
    def onchange_mecanicos_taller(self):
        taller = 0
        for mecanico in self.mecanico_ids:
            if not taller:
                taller = mecanico.taller_id
            else:
                if mecanico.taller_id != taller:
                    raise models.ValidationError('Tiene que ser el mismo taller')

        
        
        
        