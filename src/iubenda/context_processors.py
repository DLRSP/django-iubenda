"""
Context processors for Iubenda app
"""

from django.conf import settings
from django.contrib import messages
from django.contrib.sites.models import Site
from django.core.cache import cache

from .models import Iubenda


def iubenda(request):
    """Returns the info for:
    - iub_site_id: Iubenda Site ID
    - iub_policy_id: Iubenda Policy ID
    """

    cache_key = f"iubenda_{request.LANGUAGE_CODE}"
    context_cache = {}
    try:
        context_cache = cache.get(cache_key)
    except Exception as err:
        messages.warning(request, err)
        context_cache = {}

    if not context_cache or context_cache is None:
        try:
            context = {
                "cx_iubenda": Iubenda.objects.filter(site=Site.objects.get_current())
                .values("iub_site_id", "iub_policy_id")
                .get(),
            }

            cx_iubenda_options = getattr(settings, "IUBENDA_OPTIONS", False)
            if cx_iubenda_options:
                context.update({"cx_iubenda_options": cx_iubenda_options})

            cx_iubenda_nonce = getattr(settings, "IUBENDA_CSP_NONCE", False)
            if cx_iubenda_nonce:
                context.update({"cx_iubenda_nonce": cx_iubenda_nonce})

            context_cache = cache.set(cache_key, context, timeout=86400)
            return context
        except Exception as err:
            messages.error(request, err)
    return context_cache
