from odoo import fields, models


class AddPublisher(models.TransientModel):
    _name = 'publisher.wizard'
    _description = 'Add Publisher Wizard'

    publisher_id = fields.Many2one('library.publisher')
    book_id = fields.Many2one('library.book')

    def action_add_publisher(self):
        self.book_id.publisher_id = self.publisher_id.id
