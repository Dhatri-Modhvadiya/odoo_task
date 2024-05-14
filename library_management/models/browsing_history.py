from odoo import models, fields

class HistoryInformation(models.Model):
    _name = "history.info"
    _description = "this model is about History Information"

    book_borrowed = fields.Char(string="Book_Borrowed", required=True)
    reserved_by = fields.Char(string="Reserved_by", required=True)
    borrowed_date = fields.Date(string="Borrowed_Date")
    due_date = fields.Date(string="Due_Date")
