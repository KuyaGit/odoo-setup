# Odoo Development Setup (Docker Compose)

This guide explains how to set up **Odoo for local development** using **Docker Compose**.
The goal is to make Odoo easy to run, consistent across machines, and developer-friendly without installing dependencies directly on your host OS.

---

## 🚀 Why Docker for Odoo Development?

Instead of manually installing Python, PostgreSQL, system libraries, and wkhtmltopdf on your machine, this setup:

- 🐳 Uses **Docker Compose** to orchestrate services
- 🧪 Keeps your local machine clean
- 🔁 Ensures consistent environments across developers
- ⚡ Enables fast onboarding and easy rebuilds

---

## 🛠 Tools Required

Make sure you have the following installed:

- **Git**
- **Docker**
- **Docker Compose** (v2+ recommended)

> 💡 You do **not** need to install Python or PostgreSQL locally — Docker handles everything.

---

## 📁 Project Structure (Simplified)

```text
odoo/
├── docker-compose.yml
├── Dockerfile
├── odoo.conf
├── requirements.txt
└── (Odoo source code)
```

---

## 🧩 Step 1: Clone the Odoo Repository

Clone the official Odoo repository with a shallow clone for faster download.

```bash
git clone https://github.com/odoo/odoo.git \
  --depth 1 \
  --branch <latest_version_number> \
  --single-branch <directory_name>
```

**Example:**

```bash
git clone https://github.com/odoo/odoo.git \
  --depth 1 \
  --branch 17.0 \
  --single-branch odoo
```

Then move into the directory:

```bash
cd odoo
```

---

## 🐳 Step 2: Docker Compose Configuration

We use **Docker Compose** to run:

- **PostgreSQL 15** (database)
- **Odoo** (application server)

### `docker-compose.yml`

```yaml
services:
  db:
    image: postgres:15
    container_name: odoo_db
    restart: unless-stopped
    environment:
      POSTGRES_DB: postgres
      POSTGRES_USER: odoo
      POSTGRES_PASSWORD: odoo
    volumes:
      - pgdata:/var/lib/postgresql/data

  odoo:
    container_name: odoo
    build:
      context: .
      dockerfile: Dockerfile
    depends_on:
      - db
    ports:
      - "8069:8069"
    volumes:
      - .:/opt/odoo
      - odoo-data:/var/lib/odoo
    environment:
      PYTHONUNBUFFERED: "1"
    restart: unless-stopped

volumes:
  pgdata:
  odoo-data:
```

### 🔍 What This Does

- **db service**
  - Runs PostgreSQL 15
  - Persists data using Docker volumes

- **odoo service**
  - Builds a custom image via `Dockerfile`
  - Mounts source code for live development
  - Exposes Odoo on **[http://localhost:8069](http://localhost:8069)**

---

## 🧱 Step 3: Dockerfile Explanation

The Dockerfile builds a **production-like but development-friendly** Odoo environment.

### Key Responsibilities

- Uses **Python 3.12 slim** base image
- Installs all **system dependencies required by Odoo**
- Installs **wkhtmltopdf** (patched version required by Odoo)
- Uses a **non-root `odoo` user** for security
- Creates a **Python virtual environment**
- Installs Python dependencies from `requirements.txt`
- Runs Odoo using `odoo-bin`

### `Dockerfile`

```dockerfile
# Use official Python base image
FROM python:3.12-slim

# Prevent Python from writing pyc files and enable logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

ENV PATH="/home/odoo/.local/bin:$PATH"

# Install system dependencies required by Odoo
RUN apt-get update && apt-get install -y \
  git \
  build-essential \
  libpq-dev \
  python3-dev \
  libxml2-dev \
  libxslt1-dev \
  libldap2-dev \
  libsasl2-dev \
  libjpeg-dev \
  libssl-dev \
  zlib1g-dev \
  libffi-dev \
  nodejs \
  npm \
  curl \
  ca-certificates \
  fontconfig \
  xfonts-base \
  xfonts-75dpi \
  libxrender1 \
  libxext6 \
  libfreetype6 \
  fonts-noto \
  fonts-noto-cjk \
  fonts-noto-color-emoji \
  wget \
  python3-venv \
  && rm -rf /var/lib/apt/lists/*

# Install wkhtmltopdf (patched build required by Odoo)
RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.bookworm_arm64.deb \
  && apt-get update \
  && apt-get install -y ./wkhtmltox_0.12.6.1-3.bookworm_arm64.deb \
  && rm wkhtmltox_0.12.6.1-3.bookworm_arm64.deb \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Install less compiler for Odoo assets
RUN npm install -g less less-plugin-clean-css

# Create Odoo user
RUN useradd -m -d /home/odoo -s /bin/bash odoo

# Create directories
RUN mkdir -p /opt/odoo /var/lib/odoo /etc/odoo \
  && chown -R odoo:odoo /opt/odoo /var/lib/odoo /etc/odoo

USER odoo
WORKDIR /opt/odoo

# Create Python virtual environment
RUN python3 -m venv /home/odoo/odoo-venv
ENV VIRTUAL_ENV=/home/odoo/odoo-venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy requirements
COPY --chown=odoo:odoo requirements.txt .

RUN pip install setuptools wheel cython
RUN pip install --no-cache-dir -r requirements.txt

# Copy Odoo config
COPY --chown=odoo:odoo odoo.conf /etc/odoo/odoo.conf

# Copy source code
COPY --chown=odoo:odoo . /opt/odoo

EXPOSE 8069 8071

CMD ["/home/odoo/odoo-venv/bin/python", "/opt/odoo/odoo-bin", "--config=/etc/odoo/odoo.conf", "--data-dir=/var/lib/odoo"]
```

---

## ⚙️ Step 4: Odoo Configuration (`odoo.conf`)

This configuration matches the PostgreSQL service defined in `docker-compose.yml`.

### `odoo.conf`

```ini
[options]
admin_passwd = admin

; Database configuration
\db_host = db
db_port = 5432
db_user = odoo
db_password = odoo

; Paths
data_dir = /var/lib/odoo
addons_path = /opt/odoo/addons

; Server settings
xmlrpc_port = 8069
longpolling_port = 8071

; Development options
log_level = info
dev_mode = reload
```

---

## ▶️ Step 5: Start Odoo

Build and start the containers:

```bash
docker-compose up -d
```

### Useful Commands

```bash
# View logs
docker-compose logs -f odoo

# Stop containers
docker-compose down

# Rebuild images
docker-compose up -d --build
```

---

## 🌐 Access Odoo

Once running, open your browser:

```
http://localhost:8069
```

- Create a new database
  <img width="1470" height="872" alt="image" src="https://github.com/user-attachments/assets/27323cdc-1001-47f5-b01e-9287d0fc0017" />
- Login with your admin credentials
- Start developing 🎉

---
## 📄 About the Sample Addon: `custom_addons/sample_app/README.md`

While this main README explains the project-wide Odoo Docker setup, you'll also find **addon-specific documentation** in the `custom_addons/sample_app` directory.

Inside `custom_addons/sample_app/`, there's a dedicated `README.md` file. This addon-level README gives details about:
- The purpose and features of the sample addon
- Its custom model, views, and menus
- Installation and development tips for extending or adapting the addon

If you're interested in exploring, customizing, or learning about Odoo addon development, be sure to check out:
```
custom_addons/sample_app/README.md
```
for a focused guide on the addon itself, including technical and functional documentation.


---

## ✅ Summary

✔ Docker Compose manages PostgreSQL and Odoo
✔ Dockerfile ensures a clean, reproducible environment
✔ Volumes persist data and enable live development
✔ Ideal for local development and team onboarding

---

Happy coding with Odoo 🚀
