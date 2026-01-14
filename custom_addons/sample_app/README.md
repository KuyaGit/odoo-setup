# Sample App - Odoo 19 Custom Addon

A beginner-friendly demonstration addon for Odoo 19 that showcases the fundamentals of Odoo module development.

## 📋 Overview

This addon demonstrates:
- ✅ Creating a custom model with various field types
- ✅ Building list (tree) and form views
- ✅ Defining search views with filters
- ✅ Creating menus and actions
- ✅ Setting up security access rules

**Perfect for beginners learning Odoo development!**

---

## 📁 Folder Structure

```
sample_app/
├── __manifest__.py          # Addon metadata and configuration
├── __init__.py              # Python package initializer
├── README.md                # This documentation file
│
├── models/                  # Python model definitions
│   ├── __init__.py          # Models package initializer
│   └── sample_model.py      # Our custom model class
│
├── views/                   # XML view definitions
│   └── sample_model_views.xml   # List, form, search views + menus
│
└── security/                # Access control rules
    └── ir.model.access.csv  # Model access permissions
```

### File Purposes

| File | Purpose |
|------|---------|
| `__manifest__.py` | Tells Odoo about the addon (name, version, dependencies, files to load) |
| `__init__.py` | Makes the folder a Python package; imports sub-modules |
| `models/sample_model.py` | Defines the database model and its fields |
| `views/sample_model_views.xml` | Defines how data is displayed (list, form) and navigation (menus) |
| `security/ir.model.access.csv` | Controls who can read/write/create/delete records |

---

## 🚀 Installation Guide

### Prerequisites

- Odoo 19 installed and running
- Access to Odoo's custom addons folder
- Administrator access to Odoo

### Step 1: Copy the Addon

Copy the `sample_app` folder to your Odoo custom addons directory:

```bash
# Common locations:
# Linux/Mac: /opt/odoo/custom-addons/ or ~/odoo/custom-addons/
# Windows: C:\odoo\custom-addons\

cp -r sample_app /path/to/your/odoo/custom-addons/
```

### Step 2: Update Odoo Configuration

Ensure your `odoo.conf` file includes the custom addons path:

```ini
[options]
addons_path = /opt/odoo/odoo/addons,/opt/odoo/custom-addons
```

### Step 3: Restart Odoo

```bash
# If using systemd:
sudo systemctl restart odoo

# If running directly:
./odoo-bin -c /path/to/odoo.conf
```

### Step 4: Enable Developer Mode

1. Log into Odoo as an administrator
2. Go to **Settings**
3. Scroll to the bottom
4. Click **Activate the developer mode**

Or add `?debug=1` to your URL:
```
http://localhost:8069/web?debug=1
```

### Step 5: Update Apps List

1. Go to **Apps** menu
2. Click **Update Apps List** (requires developer mode)
3. Click **Update** in the popup

### Step 6: Install the Addon

1. Go to **Apps** menu
2. Remove the "Apps" filter in the search bar
3. Search for "Sample App"
4. Click **Install**

---

## 🔄 Upgrading the Module

When you make changes to the addon, you need to upgrade it:

### Method 1: From UI

1. Go to **Apps** menu
2. Search for "Sample App"
3. Click the **⋮** (three dots) menu on the addon card
4. Click **Upgrade**

### Method 2: From Command Line

```bash
./odoo-bin -c /path/to/odoo.conf -u sample_app -d your_database_name --stop-after-init
```

### Method 3: From URL (Developer Mode)

Visit: `http://localhost:8069/web?debug=1#action=base.open_module_tree`

Then search and upgrade the module.

### When to Upgrade?

| Change Type | Action Needed |
|-------------|---------------|
| Python model changes | Upgrade module |
| XML view changes | Upgrade module |
| Security CSV changes | Upgrade module |
| Static files (CSS, JS) | Clear browser cache |
| `__manifest__.py` changes | Upgrade module |

---

## 📊 Understanding the Model

### Model Definition

The `sample.model` creates a database table with these fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | Char | Yes | Short text name for the record |
| `description` | Text | No | Long text for detailed notes |
| `active` | Boolean | No | Archive toggle (default: True) |
| `create_date` | Datetime | Auto | When record was created |

### Python Code Explained

```python
class SampleModel(models.Model):
    _name = 'sample.model'        # Technical name (creates table: sample_model)
    _description = 'Sample Model'  # Human-readable name
    _order = 'create_date desc'    # Default sorting

    name = fields.Char(required=True)    # Required text field
    description = fields.Text()          # Optional long text
    active = fields.Boolean(default=True) # Archive functionality
```

---

## 🎨 Understanding the Views

### List (Tree) View

Displays records in a table format:

```xml
<list string="Sample Models">
    <field name="name"/>
    <field name="active" widget="boolean_toggle"/>
    <field name="create_date"/>
</list>
```

### Form View

For creating/editing single records:

```xml
<form string="Sample Model">
    <sheet>
        <div class="oe_title">
            <h1><field name="name"/></h1>
        </div>
        <group>
            <field name="active"/>
            <field name="description"/>
        </group>
    </sheet>
</form>
```

### Search View

Defines search and filter options:

```xml
<search string="Sample Models">
    <field name="name"/>
    <filter string="Active" domain="[('active', '=', True)]"/>
    <filter string="Archived" domain="[('active', '=', False)]"/>
</search>
```

---

## 🔒 Understanding Security

### Access Control (ir.model.access.csv)

The CSV file controls CRUD permissions:

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_sample_model_user,sample.model.user,model_sample_model,base.group_user,1,1,1,1
```

| Column | Meaning |
|--------|---------|
| `id` | Unique identifier for this rule |
| `name` | Human-readable rule name |
| `model_id:id` | Model to apply rules to (`model_` + model name with `_`) |
| `group_id:id` | User group this rule applies to |
| `perm_read` | 1 = can read, 0 = cannot read |
| `perm_write` | 1 = can update, 0 = cannot update |
| `perm_create` | 1 = can create, 0 = cannot create |
| `perm_unlink` | 1 = can delete, 0 = cannot delete |

### Common Groups

| Group | Description |
|-------|-------------|
| `base.group_user` | All internal users (employees) |
| `base.group_portal` | Portal users (external) |
| `base.group_public` | Public/anonymous users |
| `base.group_system` | Settings/Admin users |

---

## 🛠️ Extending This Addon

### Adding New Fields

1. Edit `models/sample_model.py`:
```python
priority = fields.Selection([
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
], default='medium')
```

2. Add to views in `views/sample_model_views.xml`
3. Upgrade the module

### Adding Relationships

```python
# Many2one (Foreign Key)
partner_id = fields.Many2one('res.partner', string='Customer')

# One2many (Reverse relation)
line_ids = fields.One2many('sample.model.line', 'sample_id')

# Many2many
tag_ids = fields.Many2many('sample.tag', string='Tags')
```

---

## ❓ Troubleshooting

### Module Not Appearing

1. Check the addons path in `odoo.conf`
2. Ensure `__manifest__.py` has correct syntax
3. Update Apps List in developer mode
4. Check Odoo logs for errors

### Access Denied Errors

1. Verify security CSV is listed in `__manifest__.py`
2. Check CSV syntax (proper quotes, no extra spaces)
3. Upgrade the module

### Views Not Loading

1. Check XML syntax (use an XML validator)
2. Ensure view model matches your model `_name`
3. Check Odoo logs for parsing errors

### Changes Not Appearing

1. Upgrade the module (not just restart)
2. Clear browser cache
3. In developer mode: Assets > Regenerate Assets

---
**Happy Odoo Development! 🎉**
