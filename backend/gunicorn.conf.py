import os

# Gunicorn config variables
workers = 4
bind = "0.0.0.0:10000"  # Use a specific port
timeout = 120