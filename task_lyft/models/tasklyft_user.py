from odoo import fields, models

class tasklyft_user(models.Model):
    _inherit = 'res.partner'
    
    service_id = fields.One2many('tasklyft.service', 'user_id', string='Service Id')
