# -*- coding: utf-8 -*-
# Copyright 2022 - QUADIT, SA DE CV(https://www.quadit.mx)
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api,fields,models

class academia_student(models.Model):
    _name="academia.student"
    _description="Gestion de estudiante"
    name = fields.Char("Nombre",size=128)
    last_name = fields.Char("Last_name",size=128)
    photo = fields.Char("last_name",size=128)
    create_date = fields.Datetime("Fecha de creacion",readonly=True)