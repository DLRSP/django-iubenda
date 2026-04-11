"""
See PEP 386 (https://peps.python.org/pep-0386/)

Package layout:

- ``defaults`` — static defaults for API URLs, languages, timeouts, compressor flag.
- ``conf`` — resolved settings: top-level ``IUBENDA_*`` → ``APP_CONFIG['iubenda']`` → defaults
  (same pattern as ``copyai.conf`` / ``APP_CONFIG['copyai']``).
- ``api`` — policy API helpers built on django-requests-api.
"""

__version__ = "1.7.4"
__version_info__ = tuple(int(i) if i.isdigit() else i for i in __version__.split("."))
__license__ = "MIT"
__title__ = "iubenda"

__author__ = "DLRSP"
__copyright__ = "Copyright 2010-present DLRSP"

# Version synonym
VERSION = __version_info__

# Header encoding (see RFC5987)
HTTP_HEADER_ENCODING = "iso-8859-1"

# Default datetime input and output formats
ISO_8601 = "iso-8601"
