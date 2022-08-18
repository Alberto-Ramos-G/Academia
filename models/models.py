# -*- coding: utf-8 -*-
# Copyright 2022 - QUADIT, SA DE CV(https://www.quadit.mx)
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields,models,exceptions

class ResPartner(models.Model):
    _name ="res.partner"
    _inherit="res.partner"
    company_type = fields.Selection(selection_add =[('is_school','Escuela')])

class academia_student(models.Model):
    _name="academia.student"
    _description="Gestion de estudiante"
    name = fields.Char("Nombre",size=128,required=True)
    last_name = fields.Char("Last_name",size=128)
    photo = fields.Char("last_name",size=128)
    create_date = fields.Datetime("Fecha de creacion",readonly=True)
    note =  fields.Html("Comentarios")
    state = fields.Selection([
        ('draft',"Borrador"),
        ('process',"En proceso"),
        ('done',"Egresado"),
        ('cancel',"Expulsado")
        ],"Estado",default="draft")
    active = fields.Boolean("Activo",default=True)
    age = fields.Integer("Edad")
    curp = fields.Char("CURP",size=18,required=True)
    
    #Creacion de las relaciones 
    partner_id = fields.Many2one('res.partner','Escuela')
    
    @api.constrains('curp')
    def check_curp(self):
        for record in self:
            if record.curp:
                if len(record.curp) != 18:
                    raise exception.ValidationError('La curp debe ser de 18 digitos')