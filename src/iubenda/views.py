"""
Views for Iubenda app
"""

import json
import logging

import requests
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.vary import vary_on_headers

from .models import Iubenda

logger = logging.getLogger(__name__)


@require_http_methods(["GET"])
@vary_on_headers("User-Agent", "Cookie")
def privacy(request):
    context = {}
    context_cache = {}

    cache_key = f"api_iubenda_privacy_{request.LANGUAGE_CODE}"
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
            r = requests.get(
                f'https://www.iubenda.com/api/privacy-policy/{iubenda["iub_policy_id"]}',
                params=request.GET,
            )
            if r.status_code == 200:
                context = {"req_privacy": json.loads(r.content)}

            cache.set(cache_key, context, timeout=86400)
            context_cache = cache.get(cache_key)

        except Exception as err:
            logger.error("iubenda: %s", err)

    if getattr(settings, "IUBENDA_USE_COMPRESS", True):
        return render(request, "iubenda/privacy-compress.html", context_cache)
    return render(request, "iubenda/privacy.html", context_cache)


@require_http_methods(["GET"])
@vary_on_headers("User-Agent", "Cookie")
def cookie(request):
    context = {}
    context_cache = {}

    cache_key = f"api_iubenda_cookie_{request.LANGUAGE_CODE}"
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
            r = requests.get(
                f'https://www.iubenda.com/api/privacy-policy/{iubenda["iub_policy_id"]}/cookie-policy',
                params=request.GET,
            )
            if r.status_code == 200:
                context = {"req_cookie": json.loads(r.content)}

            cache.set(cache_key, context, timeout=86400)
            context_cache = cache.get(cache_key)

        except Exception as err:
            logger.error("iubenda: %s", err)
    if getattr(settings, "IUBENDA_USE_COMPRESS", True):
        return render(request, "iubenda/cookie-compress.html", context_cache)
    return render(request, "iubenda/cookie.html", context_cache)
