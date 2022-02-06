# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError


class materialSupplier(models.Model):
    _name = 'material.supplier'
    _description = 'material.supplier'

    name = fields.Char()

class material(models.Model):
    _name = 'material.material'
    _description = 'material.material'

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True)
    buy_price = fields.Float(string="Buy Price", required=True)
    type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], default='fabric', string="Type", required=True)
    supplier_id = fields.Many2one('material.supplier', string='Supplier', required=True)
    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

    @api.constrains('buy_price')
    def _check_values(self):
        if self.buy_price < 100:
            raise exceptions.ValidationError("Buy price tidak boleh kurang dari 100")
            # return {
            #     'title': 'Warning',
            #     'message': 'Buy price tidak boleh kurang dari 100',
            # }
