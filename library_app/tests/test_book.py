from odoo.tests.common import TransactionCase


class TestBook(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestBook, self).setUp()

        self.book_01_test = self.env['library.book'].create({
            'name': 'book one',
            'code': '101',
            'active': True,
            'state': 'draft',
            # 'published_date': fields.Date.today(),

        })

    def test_01_book_values(self):
        book_id = self.book_01_test
        self.assertRecordValues(book_id, [{
            'name': 'book one',
            'code': '101',
            'active': True,
            'state': 'draft',

        }])
