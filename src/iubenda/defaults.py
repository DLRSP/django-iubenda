"""
Default values for the Iubenda app.

Runtime resolution (Django ``settings`` + optional ``APP_CONFIG['iubenda']``) is in
:mod:`iubenda.conf`. Projects do not need to import this module from ``settings.py``.
"""

from __future__ import annotations

API_BASE_URL = "https://www.iubenda.com"
API_ALLOWED_LANGS = frozenset({"it", "en"})
API_FALLBACK_LANG = "en"
API_TIMEOUT = 30.0
USE_COMPRESS = True
