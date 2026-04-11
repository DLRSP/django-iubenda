"""
Context processors for Iubenda app
"""

import logging

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.cache import cache
from django.core.exceptions import ImproperlyConfigured

from .conf import (
    get_iubenda_autoblocking,
    get_iubenda_csp_nonce,
    get_iubenda_gtm,
    get_iubenda_options,
)
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

            cx_iubenda_options = get_iubenda_options()
            if cx_iubenda_options:
                context.update({"cx_iubenda_options": cx_iubenda_options})

            cx_iubenda_gtm = get_iubenda_gtm()
            if cx_iubenda_gtm:
                context.update({"cx_iubenda_gtm": cx_iubenda_gtm})

            cx_iubenda_nonce = get_iubenda_csp_nonce()
            if cx_iubenda_nonce:
                context.update({"cx_iubenda_nonce": cx_iubenda_nonce})

            cx_iubenda_autoblocking = get_iubenda_autoblocking()
            if cx_iubenda_autoblocking:
                context.update({"cx_iubenda_autoblocking": cx_iubenda_autoblocking})

            context_cache = cache.set(cache_key, context, timeout=86400)
            return context
        except Iubenda.DoesNotExist as err:
            logger.error(
                "iubenda: before enable "
                '"iubenda.context_processors.iubenda" in your settings '
                "be sure to configure your Iubenda Site's ID inside the database! %s",
                err,
            )
            raise ImproperlyConfigured(
                "iubenda: before enable ",
                '"iubenda.context_processors.iubenda" in your settings, ',
                f"be sure to configure your Iubenda Site's ID inside the database! {err}",
            ) from err
        except Exception as err:
            logger.error("iubenda: %s", err)
            raise ImproperlyConfigured(err) from err
    return context_cache
