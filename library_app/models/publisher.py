from odoo import fields, models


class Publisher(models.Model):
    _name = 'library.publisher'
    _description = 'Publisher'
    _rec_name = 'f_name'

    f_name = fields.Char('First Name')
    l_name = fields.Char('Last Name')
    date_join = fields.Date()
    active = fields.Boolean(default=True)
    national_id = fields.Char('National ID')
    image = fields.Binary()
    book_ids = fields.One2many('library.book', inverse_name='publisher_id')
    new_book_ids = fields.Many2many('library.book')
