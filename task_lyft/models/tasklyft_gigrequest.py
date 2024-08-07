from odoo import fields, models

class tasklyft_gigrequest(models.Model):
    _name = 'tasklyft.gigrequest'
    _description = 'TaskLyft Gig Request'

    title = fields.Char(string='Title', required=True)
    is_educator = fields.Boolean(string='Do you want to teach educational courses?', default=False)
    education_category = fields.Selection([
        ('Matric', 'Matric'), 
        ('FSC(Pre-Engineering)', 'FSC(Pre-Engineering)'), 
        ('FSC(Pre-Medical)', 'FSC(Pre-Medical)'), 
        ('ICS', 'ICS'), 
        ('FA', 'FA'), 
        ('I.COM', 'I.COM'),
    ], string='Education Category')
    skill_category = fields.Selection([
        ('Python', 'Python'), 
        ('Java', 'Java'), 
        ('C++', 'C++'), 
        ('Web Development', 'Web Development'), 
        ('Data Science', 'Data Science'), 
        ('Machine Learning', 'Machine Learning'), 
        ('Database Management', 'Database Management'),
    ], string='Skill Category')
    experience_level = fields.Selection([
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'), 
        ('Professional', 'Professional')
    ], string='Experience Level')
    picture = fields.Image(string='Picture', required=True)    
    monthly_price = fields.Float(string='Price Per Month(PKR)', required=True)
    user_id = fields.Many2one('res.partner', string="User")
    
    
    status = fields.Char(string="Status")

    def action_accept_request(self):
        for record in self:
            self.env['tasklyft.service'].create({
                'title': record.title,
                'category': record.category,
                'experience_level': record.experience_level,
                'picture': record.picture,
                'price_per_hour': record.price_per_hour,
                'user_id': record.user_id.id,
            })
            # Add logic to handle rejection
            record.status = 'accepted'
        
        # redirect('../')



    
    def action_reject_request(self):
        for record in self:
            # Add logic to handle rejection
            record.status = 'rejected'
