"""gunicorn WSGI server configuration."""
import os
from multiprocessing import cpu_count

# pylint: disable=invalid-name
max_requests = 1000
# bind = os.getenv("BACKEND_HOST") + ":" + os.getenv("BACKEND_PORT")
workers = cpu_count() * 2 + 1
reload = os.getenv("WEBAPP_RELOAD", False)
timeout = int(os.getenv("GUNICORN_REQUEST_TIMEOUT", 120))
