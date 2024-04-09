"""
Context processors for Iubenda app
"""

import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.cache import cache

from .models import Iubenda

logger = logging.getLogger(__name__)


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
                "cx_iubenda": Iubenda.objects.filter(site=get_current_site(request))
                .values("iub_site_id", "iub_policy_id")
                .get(),
            }

            cx_iubenda_options = getattr(settings, "IUBENDA_OPTIONS", False)
            if cx_iubenda_options:
                context.update({"cx_iubenda_options": cx_iubenda_options})

            cx_iubenda_gtm = getattr(settings, "IUBENDA_GTM", False)
            if cx_iubenda_gtm:
                context.update({"cx_iubenda_gtm": cx_iubenda_gtm})

            cx_iubenda_nonce = getattr(settings, "IUBENDA_CSP_NONCE", False)
            if cx_iubenda_nonce:
                context.update({"cx_iubenda_nonce": cx_iubenda_nonce})

            cx_iubenda_autoblocking = getattr(settings, "IUBENDA_AUTOBLOCKING", False)
            if cx_iubenda_nonce:
                context.update({"cx_iubenda_autoblocking": cx_iubenda_autoblocking})

            context_cache = cache.set(cache_key, context, timeout=86400)
            return context
        except Exception as err:
            logger.error("iubenda: %s", err)
    return context_cache
