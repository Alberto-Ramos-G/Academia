# -*- coding: utf-8 -*-
# Copyright 2022 - QUADIT, SA DE CV(https://www.quadit.mx)
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
   "name":"Modulo Academia QUADIT",
   "version":"15.0.0",
   "depends":["base", "sale_management","account","stock"],
   "author":("QUADIT"),
   "licence":"AGPL-3",
   "summary":"""Modulo de practica QUADIT""",
   "website":"www.quedit.mx",
  "data":[
        "security/ir.model.access.csv",
        "views/view.xml",
         ],
   "installable":True,
   "auto_install":False,
}