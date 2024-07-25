from dateutil.relativedelta import relativedelta

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    """ rec name => if there is no name field"""
    _sql_constraints = [
        ('unique_name', 'unique("name")', 'This name is exist')
    ]

    name = fields.Char()
    ref = fields.Char(default='New')
    code = fields.Char(tracking=True)
    active = fields.Boolean(default=True)
    published_date = fields.Date()
    age = fields.Integer(compute='_compute_age')
    state = fields.Selection([
        ('draft', 'DRAFT'),
        ('confirm', 'CONFIRM'),
        ('published', 'PUBLISHED'),

    ], default='draft')
    image = fields.Binary()
    publisher_id = fields.Many2one('library.publisher')
    line_ids = fields.One2many('library.book.line', 'book_id')

    # @api.constrains('publisher_id')
    # def _check_publisher_id(self):
    #     for rec in self:
    #         if not rec.publisher_id:
    #             raise ValidationError("publish required ...")
    def action_add_publisher(self):
        action = self.env['ir.actions.actions']._for_xml_id('library_app.publisher_wizard_action')
        action['context'] = {'default_book_id': self.id}
        return action

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_confirmed(self):
        for rec in self:
            rec.state = 'confirm'

    def action_published(self):
        for rec in self:
            rec.state = 'published'

    @api.model
    def create(self, vals):
        res = super(Book, self).create(vals)
        res.ref = self.env['ir.sequence'].next_by_code('book_ref_seq')
        return res

    def write(self, vals):
        res = super(Book, self).write(vals)
        print("writeeeeeeeeeeeeeeee")

        return res

    def unlink(self):
        res = super(Book, self).unlink()
        print("deletteee")

        return res

    @api.model
    def _search(self, args, offset=0, limit=None, order=None):
        res = super(Book, self)._search(args, offset=0)
        print("searchhhhh")

        return res

    @api.onchange('code')
    def _onchange_code(self):
        for book in self:
            print("changeeeeeeeeeeee", book)

    @api.depends('published_date')
    def _compute_age(self):
        for rec in self:
            if rec.published_date:
                rec.age = relativedelta(fields.Date.today(), rec.published_date).months

            else:
                rec.age = False

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.name} - {rec.code}"

    def server_published_state(self):
        for rec in self:
            rec.state = 'published'

    # @api.model
    # def archive_book(self):
    #     book_ids = self.env['library.book'].search([])
    #     print(book_ids)
    #     for book in book_ids :
    #         #if condition :
    #             #book.activ=Fals
    #



class BookLine(models.Model):
    _name = 'library.book.line'
    _description = 'Book Line'

    name = fields.Char()
    date = fields.Char()
    discription = fields.Char()
    book_id = fields.Many2one('library.book')
