from odoo import models, api

class HrExpense(models.Model):
    _inherit = 'hr.expense'

    @api.model
    def custom_list_button_method(self):
        # Implement the logic for your custom button action
        return True



