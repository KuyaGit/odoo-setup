# -*- coding: utf-8 -*-
# =============================================================================
# SAMPLE MODEL DEFINITION
# =============================================================================
# This file defines a custom Odoo model (database table).
#
# Key Concepts:
# - A "model" in Odoo represents a database table
# - The model name (e.g., 'sample.model') uses dots as separators
# - Odoo automatically creates the table 'sample_model' (dots → underscores)
# - Fields define the columns in the database table
# - The ORM (Object-Relational Mapping) handles all database operations
# =============================================================================

from odoo import models, fields, api


class SampleModel(models.Model):
    """
    Sample Model - A demonstration of Odoo model creation.
    
    This model showcases:
    - Basic field types (Char, Text, Boolean, Datetime)
    - Field attributes (required, default, readonly)
    - The _name attribute (model identifier)
    - The _description attribute (human-readable name)
    
    Database Table: This class creates a table named 'sample_model'
    """
    
    # =========================================================================
    # MODEL ATTRIBUTES
    # =========================================================================
    
    # _name: Technical name of the model (REQUIRED)
    # - Used to reference this model in code and XML
    # - Convention: lowercase, words separated by dots
    # - Creates database table: 'sample_model' (dots become underscores)
    _name = 'sample.model'
    
    # _description: Human-readable name shown in logs and error messages
    # - Always provide this for clarity
    _description = 'Sample Model'
    
    # _order: Default sorting when records are displayed
    # - Format: 'field_name ASC/DESC, field_name2 ASC/DESC'
    # - Default is 'id' if not specified
    _order = 'create_date desc, name'
    
    # =========================================================================
    # FIELD DEFINITIONS
    # =========================================================================
    # Each field becomes a column in the database table.
    # Odoo provides many field types - here are some common ones:
    
    # -------------------------------------------------------------------------
    # name - Character Field (VARCHAR in database)
    # -------------------------------------------------------------------------
    # Char: Short text field, single line
    # - 'string': Label shown in UI (optional, defaults to field name capitalized)
    # - 'required': If True, field cannot be empty
    # - 'help': Tooltip text shown when hovering over the field
    # - 'index': If True, creates database index for faster searches
    name = fields.Char(
        string='Name',
        required=True,
        help='Enter a descriptive name for this record',
        index=True,  # Improves search performance on this field
    )
    
    # -------------------------------------------------------------------------
    # description - Text Field (TEXT in database)
    # -------------------------------------------------------------------------
    # Text: Long text field, multi-line
    # - Good for notes, descriptions, or any lengthy content
    # - No practical size limit (unlike Char which has max 255 chars by default)
    description = fields.Text(
        string='Description',
        help='Detailed description of this record (optional)',
    )
    
    # -------------------------------------------------------------------------
    # active - Boolean Field (BOOLEAN in database)
    # -------------------------------------------------------------------------
    # Boolean: True/False toggle
    # - 'default': Initial value for new records (can be a value or function)
    # - The 'active' field has special meaning in Odoo:
    #   * Records with active=False are hidden by default (archived)
    #   * Users can see them using "Archived" filter
    #   * This is Odoo's standard soft-delete mechanism
    active = fields.Boolean(
        string='Active',
        default=True,
        help='Uncheck to archive this record (hide without deleting)',
    )
    
    # -------------------------------------------------------------------------
    # create_date - Datetime Field (TIMESTAMP in database)
    # -------------------------------------------------------------------------
    # Datetime: Date and time value
    # - 'readonly': If True, users cannot edit this field in the UI
    # - NOTE: 'create_date' is a magic field - Odoo automatically creates it!
    #   We're redefining it here just to add a custom string/help.
    #   Other magic fields: create_uid, write_date, write_uid
    create_date = fields.Datetime(
        string='Created On',
        readonly=True,
        help='Timestamp when this record was created (auto-filled by Odoo)',
    )
    
    # =========================================================================
    # ADDITIONAL FIELD EXAMPLES (commented out - for reference)
    # =========================================================================
    # 
    # Integer field:
    # quantity = fields.Integer(string='Quantity', default=0)
    #
    # Float field with precision:
    # price = fields.Float(string='Price', digits=(10, 2))
    #
    # Selection field (dropdown):
    # state = fields.Selection([
    #     ('draft', 'Draft'),
    #     ('confirmed', 'Confirmed'),
    #     ('done', 'Done'),
    # ], string='Status', default='draft')
    #
    # Date field (date only, no time):
    # due_date = fields.Date(string='Due Date')
    #
    # Many2one (foreign key to another model):
    # partner_id = fields.Many2one('res.partner', string='Customer')
    #
    # One2many (reverse of Many2one):
    # line_ids = fields.One2many('sample.model.line', 'sample_id', string='Lines')
    #
    # Many2many (many-to-many relationship):
    # tag_ids = fields.Many2many('sample.tag', string='Tags')
    # =========================================================================
