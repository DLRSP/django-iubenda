"""
Views for Iubenda app
"""

import json
import logging

from django.contrib.sites.models import Site
from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.vary import vary_on_headers

from .api import (
    api_request_timeout,
    get_iubenda_client,
    iubenda_request_params,
    normalize_iubenda_lang,
)
from .conf import get_iubenda_use_compress
from .models import Iubenda

logger = logging.getLogger(__name__)


def _norm_lang(request):
    return normalize_iubenda_lang(getattr(request, "LANGUAGE_CODE", None))


@require_http_methods(["GET"])
@vary_on_headers("User-Agent", "Cookie")
def privacy(request):
    context = {}
    context_cache = {}

    cache_key = f"api_iubenda_privacy_{_norm_lang(request)}"
    try:
        context_cache = cache.get(cache_key)
    except Exception as err:
        logger.warning("iubenda: %s", err)

    if not context_cache or context_cache is None:
        try:
            iubenda = (
                Iubenda.objects.filter(site=Site.objects.get_current())
                .values("iub_policy_id")
                .get()
            )
            r = get_iubenda_client().get(
                f'api/privacy-policy/{iubenda["iub_policy_id"]}',
                params=iubenda_request_params(request),
                timeout=api_request_timeout(),
            )
            if r.status_code == 200:
                context = {"req_privacy": json.loads(r.content)}

            cache.set(cache_key, context, timeout=86400)
            context_cache = cache.get(cache_key)

        except Exception as err:
            logger.error("iubenda: %s", err)

    if get_iubenda_use_compress():
        return render(request, "iubenda/privacy-compress.html", context_cache)
    return render(request, "iubenda/privacy.html", context_cache)


@require_http_methods(["GET"])
@vary_on_headers("User-Agent", "Cookie")
def cookie(request):
    context = {}
    context_cache = {}

    cache_key = f"api_iubenda_cookie_{_norm_lang(request)}"
    try:
        context_cache = cache.get(cache_key)
    except Exception as err:
        logger.warning("iubenda: %s", err)

    if not context_cache or context_cache is None:
        try:
            iubenda = (
                Iubenda.objects.filter(site=Site.objects.get_current())
                .values("iub_policy_id")
                .get()
            )
            r = get_iubenda_client().get(
                f'api/privacy-policy/{iubenda["iub_policy_id"]}/cookie-policy',
                params=iubenda_request_params(request),
                timeout=api_request_timeout(),
            )
            if r.status_code == 200:
                context = {"req_cookie": json.loads(r.content)}

            cache.set(cache_key, context, timeout=86400)
            context_cache = cache.get(cache_key)

        except Exception as err:
            logger.error("iubenda: %s", err)
    if get_iubenda_use_compress():
        return render(request, "iubenda/cookie-compress.html", context_cache)
    return render(request, "iubenda/cookie.html", context_cache)
