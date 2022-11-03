# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PatientList(models.Model):
    _name = 'patient.list'
    _description = 'LIST PATIENT'

    firstname = fields.Char(string='First Name')
    lastname = fields.Char(string='Last Name')
    name= fields.Char(compute='_compute_lastname_firstname', string='Name')
    age = fields.Integer(string='Age')
    state = fields.Selection([('new','Nouveau'),('consult','Consulter'),('treaty','Traité'),('cancelled','Annulé')],
                              default='new')
    
    @api.depends('firstname', 'lastname')
    def _compute_lastname_firstname(self):
        for result in self:
            result.name = result.firstname+" "+result.lastname if result.lastname != False else result.firstname
    
    def open_wizard(self):
          return {
               'name':('Test Window Action'),
               'view_mode': 'form',
               'res_model': 'patient.popup',
               'type': 'ir.actions.act_window',
               'target': 'new'
          }

    def set_consult(self):
        self.state = 'consult'
    def set_treaty(self):
        self.state = 'treaty'
    def set_cancelled(self):
        self.state = 'cancelled'
    def set_renew(self):
        self.state = 'new'