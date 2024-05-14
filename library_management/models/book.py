from odoo import models, fields

class BookInformation(models.Model):
    _name = "book.info"
    _description = "this model is about Book Information"

    book_name = fields.Char(string="Book_Name", required=True)
    book_price = fields.Float(string="Book_Price")
    publication_date = fields.Date(string="Publication_Date")
