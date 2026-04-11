# HTTP client and policy API

This tutorial describes how django-iubenda loads **privacy** and **cookie** policy content from Iubenda’s HTTP API, and how you can reuse the same patterns in your own code.

## Overview

- Policy pages are built from JSON returned by Iubenda’s public endpoints.
- Outbound calls use **[django-requests-api](https://pypi.org/project/django-requests-api/)** (`requests_api`): a small client with a configurable base URL and optional shared instances per host.
- Query parameters sent to the API are built from the incoming Django request: existing GET keys are preserved, and **`lang`** is set from the active locale using a safe, configurable mapping.

Install dependencies as documented for your django-iubenda version (see the project `requirements` / packaging metadata). Register **`requests_api`** and **`iubenda`** in `INSTALLED_APPS` (see [Installation](../index.md#installation)).

## Public imports

Prefer importing from the **`requests_api`** package namespace:

```python
from requests_api import (
    RequestsApi,
    copy_get_params_with_overrides,
    normalize_api_language,
    requests_api_for_base,
)
```

django-iubenda’s own glue lives in **`iubenda.api`** (see below).

## Settings (and `APP_CONFIG`)

Values are resolved by **`iubenda.conf`**: top-level `IUBENDA_*` first (non-empty strings), then **`APP_CONFIG["iubenda"]`** (keys `API_BASE_URL`, `API_ALLOWED_LANGS`, `API_FALLBACK_LANG`, `API_TIMEOUT`), then defaults. See [Configuration](configuration.md).

| Setting / `APP_CONFIG` key | Default | Description |
|---------------------------|---------|-------------|
| `IUBENDA_API_BASE_URL` / `API_BASE_URL` | `https://www.iubenda.com` | Base URL for Iubenda API requests. |
| `IUBENDA_API_ALLOWED_LANGS` / `API_ALLOWED_LANGS` | `it`, `en` | Iterable of `lang` values your policies support. |
| `IUBENDA_API_FALLBACK_LANG` / `API_FALLBACK_LANG` | `en` | `lang` when the active Django language is not in the allowed set. |
| `IUBENDA_API_TIMEOUT` / `API_TIMEOUT` | `30` | Timeout (seconds) for each API call. |

Adjust the language settings if your Iubenda account publishes policies in more languages.

**django-requests-api** also supports **`APP_CONFIG["requests_api"]`** and **`REQUESTS_API_*`** for client cache size and an optional default-timeout helper. Those settings do **not** override **`IUBENDA_API_TIMEOUT`** / **`API_TIMEOUT`** for policy requests; those stay in **`iubenda.conf`**. See [Configuration](configuration.md).

## Helpers in `iubenda.api`

These functions use **`iubenda.conf`** (so `APP_CONFIG["iubenda"]` and `IUBENDA_*` both apply) and compose the HTTP client and query string:

```python
from iubenda.api import (
    api_request_timeout,
    get_iubenda_client,
    iubenda_request_params,
    normalize_iubenda_lang,
)
```

- **`normalize_iubenda_lang`** — maps a Django language code to an allowed API `lang`.
- **`iubenda_request_params`** — copy of `request.GET` with `lang` set from `request.LANGUAGE_CODE`.
- **`get_iubenda_client`** — shared client for the configured API base URL.
- **`api_request_timeout`** — timeout from `iubenda.conf`.

## Reusing the same building blocks

For other HTTP integrations, you can combine the django-requests-api helpers with your own `allowed` / `fallback` and base URL:

```python
from requests_api import (
    copy_get_params_with_overrides,
    normalize_api_language,
    requests_api_for_base,
)

lang = normalize_api_language(
    getattr(request, "LANGUAGE_CODE", None),
    allowed=("it", "en", "de"),
    fallback="en",
)
params = copy_get_params_with_overrides(request, lang=lang)
client = requests_api_for_base("https://api.example.com")
response = client.get("v1/resource", params=params, timeout=30)
```

## Caching

django-iubenda caches successful API responses per normalized language. After changing API-related settings, `APP_CONFIG["iubenda"]`, or policy configuration, you may need to clear the cache (or wait for TTL) so all workers serve fresh content.
