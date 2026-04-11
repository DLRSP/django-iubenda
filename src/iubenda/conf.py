"""
Resolved Iubenda configuration (lazy reads from ``django.conf.settings``).

Priority for each value:

1. Top-level Django setting (e.g. ``IUBENDA_API_BASE_URL``), if defined and non-empty
   for strings (empty strings fall through so ``APP_CONFIG`` can supply the value).
2. Partial override inside ``settings.APP_CONFIG["iubenda"]`` (merged onto
   :mod:`iubenda.defaults`).
3. Package defaults from :mod:`iubenda.defaults`.

For booleans with default ``False`` (GTM, autoblocking), an explicit top-level
``False`` still wins over ``APP_CONFIG`` (use :func:`hasattr` / ``_UNSET`` rules below).

Example::

    APP_CONFIG = {
        "iubenda": {
            "API_BASE_URL": "https://www.iubenda.com",
            "API_ALLOWED_LANGS": ("it", "en", "de"),
            "API_FALLBACK_LANG": "en",
            "API_TIMEOUT": 45,
            "USE_COMPRESS": True,
            "OPTIONS": {"countryDetection": "true"},
            "GTM": True,
            "CSP_NONCE": "nonce-from-csp",
            "AUTOBLOCKING": True,
        },
    }

    IUBENDA_API_TIMEOUT = 60  # overrides APP_CONFIG for this key only
"""

from __future__ import annotations

from typing import Any

from django.conf import settings

from . import defaults

_UNSET = object()


def _app_config_iubenda() -> dict[str, Any]:
    cfg = getattr(settings, "APP_CONFIG", None) or {}
    block = cfg.get("iubenda")
    return dict(block) if isinstance(block, dict) else {}


def _get_str(
    django_name: str,
    nested_keys: tuple[str, ...],
    fallback: str,
) -> str:
    v = getattr(settings, django_name, _UNSET)
    if v is not _UNSET and v is not None and str(v).strip() != "":
        return str(v)
    nested = _app_config_iubenda()
    for key in nested_keys:
        x = nested.get(key)
        if x is not None and str(x).strip() != "":
            return str(x)
    return fallback


def get_iubenda_api_base_url() -> str:
    return _get_str(
        "IUBENDA_API_BASE_URL",
        ("API_BASE_URL", "IUBENDA_API_BASE_URL"),
        defaults.API_BASE_URL,
    ).strip() or defaults.API_BASE_URL


def get_iubenda_api_allowed_langs() -> frozenset[str]:
    if hasattr(settings, "IUBENDA_API_ALLOWED_LANGS"):
        raw = settings.IUBENDA_API_ALLOWED_LANGS
        if raw is not None:
            return frozenset(str(x).strip().lower() for x in raw if str(x).strip())
    nested = _app_config_iubenda().get("API_ALLOWED_LANGS")
    if nested is not None:
        return frozenset(str(x).strip().lower() for x in nested if str(x).strip())
    return frozenset(defaults.API_ALLOWED_LANGS)


def get_iubenda_api_fallback_lang() -> str:
    fb = _get_str(
        "IUBENDA_API_FALLBACK_LANG",
        ("API_FALLBACK_LANG", "IUBENDA_API_FALLBACK_LANG"),
        defaults.API_FALLBACK_LANG,
    ).strip().lower()
    return fb or defaults.API_FALLBACK_LANG


def get_iubenda_api_timeout() -> float:
    v = getattr(settings, "IUBENDA_API_TIMEOUT", _UNSET)
    if v is not _UNSET and v is not None:
        return float(v)
    nested = _app_config_iubenda().get("API_TIMEOUT")
    if nested is not None:
        return float(nested)
    return float(defaults.API_TIMEOUT)


def get_iubenda_use_compress() -> bool:
    v = getattr(settings, "IUBENDA_USE_COMPRESS", _UNSET)
    if v is not _UNSET:
        return bool(v)
    nested = _app_config_iubenda()
    if "USE_COMPRESS" in nested and nested["USE_COMPRESS"] is not None:
        return bool(nested["USE_COMPRESS"])
    return bool(defaults.USE_COMPRESS)


def get_iubenda_options():
    """Dict of Iubenda script options, or a falsey value if not configured."""
    if hasattr(settings, "IUBENDA_OPTIONS"):
        v = settings.IUBENDA_OPTIONS
        if v:
            return v
        return False
    nested = _app_config_iubenda().get("OPTIONS")
    if nested:
        return nested
    return False


def get_iubenda_gtm() -> bool:
    if hasattr(settings, "IUBENDA_GTM"):
        return bool(settings.IUBENDA_GTM)
    nested = _app_config_iubenda()
    if "GTM" in nested and nested["GTM"] is not None:
        return bool(nested["GTM"])
    return False


def get_iubenda_csp_nonce():
    if hasattr(settings, "IUBENDA_CSP_NONCE"):
        v = settings.IUBENDA_CSP_NONCE
        return v if v else False
    nested = _app_config_iubenda().get("CSP_NONCE")
    return nested if nested else False


def get_iubenda_autoblocking() -> bool:
    if hasattr(settings, "IUBENDA_AUTOBLOCKING"):
        return bool(settings.IUBENDA_AUTOBLOCKING)
    nested = _app_config_iubenda()
    if "AUTOBLOCKING" in nested and nested["AUTOBLOCKING"] is not None:
        return bool(nested["AUTOBLOCKING"])
    return False
