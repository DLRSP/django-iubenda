import json

import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.sites.models import Site
from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.vary import vary_on_headers

from .models import Iubenda


@require_http_methods(["GET"])
@vary_on_headers("User-Agent", "Cookie")
def privacy(request):
    context = {}

    cache_key = f"api_iubenda_privacy_{request.LANGUAGE_CODE}"
    context_cache = None
    try:
        context_cache = cache.get(cache_key)
    except Exception as err:
        messages.warning(request, err)
        context_cache = None

    if context_cache is None:
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
            context_cache = cache.set(cache_key, context, timeout=86400)

            if getattr(settings, "IUBENDA_USE_COMPRESS", True):
                return render(request, "iubenda/privacy-compress.html", context)
            return render(request, "iubenda/privacy.html", context)
        except Exception as err:
            messages.error(request, err)
    return render(request, "iubenda/privacy.html", context_cache)


@require_http_methods(["GET"])
@vary_on_headers("User-Agent", "Cookie")
def cookie(request):
    context = {}

    cache_key = f"api_iubenda_cookie_{request.LANGUAGE_CODE}"
    context_cache = None
    try:
        context_cache = cache.get(cache_key)
    except Exception as err:
        messages.warning(request, err)
        context_cache = None

    if context_cache is None:
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
            messages.error(request, err)
    if getattr(settings, "IUBENDA_USE_COMPRESS", True):
        return render(request, "iubenda/cookie-compress.html", context_cache)
    return render(request, "iubenda/cookie.html", context_cache)
