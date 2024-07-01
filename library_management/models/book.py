from odoo import models, fields, api

class BookInformation(models.Model):
    _name = "book.info"
    _description = "this model is about Book Information"

    book_name = fields.Char(string="Book_Name", required=True)
    book_price = fields.Float(string="Book_Price")
    publication_date = fields.Date(string="Publication_Date")

    @api.model
    def create(self, vals):
        new_book = super(BookInformation, self).create(vals)
        print(new_book)  # Print the created record for verification (optional)
        return new_book

    def write(self, vals):
        # Update the records with the new values provided in vals
        result = super(BookInformation, self).write(vals)
        print(result)  # Print the updated records for verification (optional)
        return result

    def unlink(self):
        result = super(BookInformation, self).unlink()
        print(result)  # Print the deleted records for verification (optional)
        return result

    def copy(self):
        result = super(BookInformation, self).copy()
        print(result)  # Print the deleted records for verification (optional)
        return result

    # def search(self, domain=[('book_price', '>', 500)], offset=0, limit=None, order=None, count=False):
    #     result = super(BookInformation, self).search(domain, offset=offset, limit=limit, order=order, count=count)
    #     print(result)  # Print the found records for verification (optional)
    #     return result





