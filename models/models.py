# -*- coding: utf-8 -*-
# Copyright 2022 - QUADIT, SA DE CV(https://www.quadit.mx)
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields,models,exceptions

class ResPartner(models.Model):
    _name ="res.partner"
    _inherit="res.partner"
    company_type = fields.Selection(selection_add =[('is_school','Escuela'), ('student_id', 'Estudiante')])
    student_id = fields.Many2one('academia.student', 'Estudiante')

class academia_student(models.Model):
    _name="academia.student"
    _description="Gestion de estudiante"
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    name = fields.Char("Nombre",size=128,required=True,track_visibility='onchange')
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
    country = fields.Many2one('res.country','Pais',related="partner_id.country_id")
    
    #Creacion de las relaciones 
    partner_id = fields.Many2one('res.partner','Escuela')
    invoice_ids = fields.Many2many('account.move',
                                   'student invoice_rel',
                                   'student_id', 'journal_id',
                                   'Facturas')

    @api.constrains('curp')
    def check_curp(self):
        for record in self:
            if record.curp:
                if len(record.curp) != 18:
                    raise exception.ValidationError('La curp debe ser de 18 digitos')
        
    def unlink(self):
        partner_obj = self.env['res.partner'] 
        partners = partner_obj.search([('student_id', 'in', self.ids)]) 
        print("partners: ",partners) 
        if partners:
            for partner in partners: 
                partner.unlink() 
        res = super(academia_student, self).unlink()
        return res   
         
    def create(self, values):
        if values['name']:
            nombre = values['name']
            if self.env['academia.student'].search([('name', '=', self.name)]): 
                values.update({ 
                    'name': values['name']+"(copy)"
                })
        res = super(academia_student, self).create(values) 
        partner_obj = self.env['res.partner'] 
        vals_to_partner = { 
            'name': res['name']+" "+res["last_name"],
            'company_type': "student_id", 
            'student_id': res['id'],
        } 
        print(vals_to_partner) 
        partner = partner_obj.create(vals_to_partner)
        print('-->partner_id: ', partner)
        return res
