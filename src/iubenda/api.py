"""
Iubenda-specific wiring: Django settings / ``APP_CONFIG['iubenda']`` and public
names used by templates and sibling apps (e.g. ``normalize_iubenda_lang``).

Resolution order is documented in :mod:`iubenda.conf`. Generic HTTP helpers come
from **django-requests-api** (``from requests_api import …``).
"""

from __future__ import annotations

from django.http import HttpRequest
from requests_api import (
    RequestsApi,
    copy_get_params_with_overrides,
    normalize_api_language,
    requests_api_for_base,
)

from . import conf


def _allowed_langs():
    return conf.get_iubenda_api_allowed_langs()


def _fallback_lang() -> str:
    return conf.get_iubenda_api_fallback_lang()


def normalize_iubenda_lang(language_code: str | None) -> str:
    """
    Map Django ``LANGUAGE_CODE`` to an Iubenda ``lang`` query value.

    Uses :func:`requests_api.normalize_api_language` with values from
    :mod:`iubenda.conf` (``IUBENDA_API_*`` / ``APP_CONFIG['iubenda']``).
    """
    return normalize_api_language(
        language_code,
        allowed=_allowed_langs(),
        fallback=_fallback_lang(),
    )


def iubenda_request_params(request: HttpRequest):
    """
    QueryDict for HTTP GET ``params=``: copy of ``GET`` with ``lang`` forced via
    :func:`normalize_iubenda_lang`.
    """
    return copy_get_params_with_overrides(
        request,
        lang=normalize_iubenda_lang(getattr(request, "LANGUAGE_CODE", None)),
    )


def api_request_timeout() -> float:
    """Seconds for Iubenda API HTTP calls (see :func:`iubenda.conf.get_iubenda_api_timeout`)."""
    return conf.get_iubenda_api_timeout()


def get_iubenda_client() -> RequestsApi:
    """
    Shared :class:`requests_api.RequestsApi` for the configured API base URL
    (see :func:`iubenda.conf.get_iubenda_api_base_url`), via
    :func:`requests_api.requests_api_for_base`.
    """
    base = conf.get_iubenda_api_base_url().strip()
    return requests_api_for_base(base.rstrip("/"))
