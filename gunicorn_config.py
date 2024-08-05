# gunicorn_config.py
bind = "0.0.0.0:8000"  # Bind to all IP addresses on port 8000
workers = 2            # Number of worker processes
threads = 4            # Number of threads per worker
timeout = 120          # Timeout for requests
