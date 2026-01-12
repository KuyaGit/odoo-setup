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

# Install wkhtmltopdf (official patched build required by Odoo)
RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.bookworm_arm64.deb \
  && apt-get update \
  && apt-get install -y ./wkhtmltox_0.12.6.1-3.bookworm_arm64.deb \
  && rm wkhtmltox_0.12.6.1-3.bookworm_arm64.deb \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Install less compiler for Odoo assets
RUN npm install -g less less-plugin-clean-css

# Create Odoo user (do NOT run as root)
RUN useradd -m -d /home/odoo -s /bin/bash odoo

# Create directories
RUN mkdir -p /opt/odoo /var/lib/odoo /etc/odoo \
  && chown -R odoo:odoo /opt/odoo /var/lib/odoo /etc/odoo

# Switch to odoo user
USER odoo
WORKDIR /opt/odoo

# Create Python virtual environment
RUN python3 -m venv /home/odoo/odoo-venv
ENV VIRTUAL_ENV=/home/odoo/odoo-venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy Python requirements first (better layer caching)
COPY --chown=odoo:odoo requirements.txt .

# Install build tools
RUN pip install setuptools wheel cython

# Install Python dependencies in the virtual environment
RUN pip install --no-cache-dir -r requirements.txt

# Copy development Odoo config
COPY --chown=odoo:odoo odoo.conf /etc/odoo/odoo.conf

# Copy the full Odoo source code
COPY --chown=odoo:odoo . /opt/odoo

# Expose Odoo ports
EXPOSE 8069 8071

RUN pwd

# Run Odoo in development mode
# Run Odoo in development mode using virtual environment
CMD ["/home/odoo/odoo-venv/bin/python", "/opt/odoo/odoo-bin", "--config=/etc/odoo/odoo.conf", "--data-dir=/var/lib/odoo"]

