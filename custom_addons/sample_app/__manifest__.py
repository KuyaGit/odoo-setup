# -*- coding: utf-8 -*-
# =============================================================================
# ODOO ADDON MANIFEST FILE
# =============================================================================
# This file is REQUIRED for every Odoo addon. It tells Odoo:
# - Basic information about the addon (name, version, author)
# - Which other addons it depends on
# - Which data files to load (views, security, etc.)
# - The license and category
#
# Without this file, Odoo won't recognize the folder as an addon.
# =============================================================================

{
    # -------------------------------------------------------------------------
    # BASIC INFORMATION
    # -------------------------------------------------------------------------
    # 'name': Display name shown in the Apps menu
    'name': 'Sample App',
    
    # 'version': Addon version following semantic versioning
    # Format: ODOO_VERSION.ADDON_MAJOR.ADDON_MINOR
    # Example: 19.0.1.0.0 means Odoo 19, addon version 1.0.0
    'version': '19.0.1.0.0',
    
    # 'summary': Short description shown in Apps list
    'summary': 'A simple sample addon demonstrating Odoo model, views, and menus',
    
    # 'description': Detailed description (can use reStructuredText format)
    'description': """
Sample Odoo Addon
=================

This addon demonstrates:
* Creating a custom model with various field types
* Building tree (list) and form views
* Defining menus and actions
* Setting up security access rules

Perfect for beginners learning Odoo development!
    """,
    
    # 'author': Creator of the addon
    'author': 'Your Company Name',
    
    # 'website': Optional URL for more information
    'website': 'https://www.yourcompany.com',
    
    # -------------------------------------------------------------------------
    # TECHNICAL INFORMATION
    # -------------------------------------------------------------------------
    # 'category': Groups the addon in the Apps menu
    # Common categories: Sales, Inventory, Accounting, Human Resources, etc.
    'category': 'Uncategorized',
    
    # 'depends': List of addons this module requires to work
    # 'base' is the core Odoo module - always include it for basic functionality
    'depends': ['base'],
    
    # 'data': List of data files to load when the addon is installed
    # ORDER MATTERS! Load security files BEFORE views that use them
    # Files are loaded in the order listed here
    'data': [
        # Security rules must be loaded first so views can reference groups
        'security/ir.model.access.csv',
        
        # Then load views, menus, and actions
        'views/sample_model_views.xml',
    ],
    
    # 'demo': Demo data files loaded only when installing with demo data
    # Useful for showcasing features with sample records
    'demo': [],
    
    # -------------------------------------------------------------------------
    # ADDON BEHAVIOR FLAGS
    # -------------------------------------------------------------------------
    # 'installable': If True, addon appears in Apps menu and can be installed
    'installable': True,
    
    # 'application': If True, addon appears as a main app (with its own icon)
    # Set to True for full-featured applications, False for smaller modules
    'application': True,
    
    # 'auto_install': If True, installs automatically when all dependencies are met
    # Usually False - let users choose to install
    'auto_install': False,
    
    # 'license': Required license declaration
    # Common options: 'LGPL-3', 'GPL-3', 'AGPL-3', 'OPL-1' (proprietary)
    'license': 'LGPL-3',
}
