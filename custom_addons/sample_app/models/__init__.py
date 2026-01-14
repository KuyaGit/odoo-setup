# -*- coding: utf-8 -*-
# =============================================================================
# MODELS PACKAGE INITIALIZER
# =============================================================================
# This file imports all model files in the 'models' folder.
# Each model file contains one or more Odoo model classes.
#
# When you add a new model file:
# 1. Create the file (e.g., models/my_new_model.py)
# 2. Add an import here (e.g., from . import my_new_model)
#
# Without the import here, Odoo won't load your model!
# =============================================================================

# Import our sample model
# This makes the SampleModel class available to Odoo's ORM
from . import sample_model
