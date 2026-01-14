# -*- coding: utf-8 -*-


from odoo import models, fields


class SampleModel(models.Model):
    """Sample Model - A demonstration of Odoo model creation."""
    
    _name = 'sample.model'
    _description = 'Sample Model'
    _order = 'create_date desc, name'

    name = fields.Char(
        string='Name',
        required=True,
        help='Enter a descriptive name for this record',
    )
    
    description = fields.Text(
        string='Description',
        help='Detailed description of this record',
    )
    
    active = fields.Boolean(
        string='Active',
        default=True,
        help='Uncheck to archive this record',
    )
    
    # Note: create_date is automatically provided by Odoo - no need to define it
