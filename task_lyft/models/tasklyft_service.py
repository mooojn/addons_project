from odoo import fields, models

class tasklyft_service(models.Model):
    _name = 'tasklyft.service'
    _description = 'TaskLyft Service'

    title = fields.Char(string='Title', required=True)
<<<<<<< Updated upstream
    
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
    
=======
    category = fields.Selection([
        ('Matric', 'Matric'), 
        ('FSC(Pre Engineering)', 'FSC(Pre Engineering)'), 
        ('FSC(Pre Medical)', 'FSC(Pre Medical)'), 
        ('ICS', 'ICS'), 
        ('ICOM', 'ICOM'), 
        ('FA', 'FA'), 
        ('Pyhton', 'Pyhton'), 
        ('Web Development', 'Web Development'),
        ('C++', 'C++'),
        ('OOP and C#', 'OOP and C#'),
        ('ODOO Development', 'ODOO Development'),
        ('Graphic Designing', 'Graphic Designing'),
        ('Wordpress', 'Wordpress')
    ], string='Category', required=True)
>>>>>>> Stashed changes
    experience_level = fields.Selection([
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'), 
        ('Professional', 'Professional')
    ], string='Experience Level')
<<<<<<< Updated upstream
    picture = fields.Image(string='Picture', required=True)    
    monthly_price = fields.Float(string='Price Per Month(PKR)', required=True)
=======
    Location=fields.Selection([
        ('UET Lahore','UET Lahore'),
        ('Shalamar Garden','Shalamar Garden'),
        ('Model Town','Model Town'),
        ('Gulberg','Gulberg'),
        ('Town Ship','Town Ship'),
        ('Muslim Town','Muslim Town'),
        ('Wahdat Road','Wahdat Road')
        ],string='Location',required=True)
    picture = fields.Image(string='Picture', required=True)

    price_per_month = fields.Float(string='Price Per Month(PKR)', required=True)
    
>>>>>>> Stashed changes
    user_id = fields.Many2one('res.partner', string="User")
