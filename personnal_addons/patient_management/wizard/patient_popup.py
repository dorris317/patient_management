from odoo import fields, models
import datetime

class PatientPopup(models.TransientModel):
    _name = 'patient.popup'
    _rec_name = 'birth_day'

    birth_day = fields.Date(string='Birthday')

    def calcul_birthday(self):
        year_birth_patient = self.birth_day.year
        year_now = datetime.date.today().year
        patient_management = self.env['patient.list']
        active_id = self.env.context.get('active_id')
        patient_management_id =patient_management.browse(active_id)
        patient_management_id.age = year_now-year_birth_patient

