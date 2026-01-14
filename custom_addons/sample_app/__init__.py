# -*- coding: utf-8 -*-
# =============================================================================
# MAIN PACKAGE INITIALIZER
# =============================================================================
# This file makes the 'sample_app' folder a Python package.
# It imports all sub-packages (like models, controllers, wizards, etc.)
#
# When Odoo loads this addon, Python executes this file first.
# By importing 'models', Python also executes models/__init__.py,
# which in turn imports all model files.
#
# This chain of imports ensures all Python files in the addon are loaded.
# =============================================================================

# Import the models sub-package
# This triggers models/__init__.py which loads all our model classes
from . import models
