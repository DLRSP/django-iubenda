# Configuration (`APP_CONFIG` and settings)

django-iubenda reads options through **`iubenda.conf`**, using the same precedence rules as other DLRSP apps (for example **copyai**):

1. **Top-level Django settings** (`IUBENDA_*`) — for strings, empty values are ignored so `APP_CONFIG` can supply them.
2. **`settings.APP_CONFIG["iubenda"]`** — nested dict, short keys (see table below).
3. **Package defaults** in `iubenda.defaults`.

Import the resolved module if you need values in your own code:

```python
from iubenda.conf import get_iubenda_api_timeout, get_iubenda_options
```

## `APP_CONFIG["iubenda"]` keys

| Key | Maps to / same meaning as | Type / notes |
|-----|---------------------------|--------------|
| `API_BASE_URL` | `IUBENDA_API_BASE_URL` | `str` |
| `API_ALLOWED_LANGS` | `IUBENDA_API_ALLOWED_LANGS` | iterable of language codes |
| `API_FALLBACK_LANG` | `IUBENDA_API_FALLBACK_LANG` | `str` |
| `API_TIMEOUT` | `IUBENDA_API_TIMEOUT` | number (seconds) |
| `USE_COMPRESS` | `IUBENDA_USE_COMPRESS` | `bool` (compressor templates) |
| `OPTIONS` | `IUBENDA_OPTIONS` | `dict` (Iubenda script options) |
| `GTM` | `IUBENDA_GTM` | `bool` |
| `CSP_NONCE` | `IUBENDA_CSP_NONCE` | `str` or falsey |
| `AUTOBLOCKING` | `IUBENDA_AUTOBLOCKING` | `bool` |

## Example

```python
# settings.py
APP_CONFIG = {
    "iubenda": {
        "API_ALLOWED_LANGS": ("it", "en", "de"),
        "API_FALLBACK_LANG": "en",
        "API_TIMEOUT": 45,
        "GTM": True,
        "OPTIONS": {
            "countryDetection": "true",
            "perPurposeConsent": "true",
        },
    },
}

# Optional: override a single value at top level
IUBENDA_API_BASE_URL = "https://www.iubenda.com"
```

Secrets are not required for these keys; keep policy IDs in the database via the **Iubenda** admin model as usual.

## Related: `APP_CONFIG["requests_api"]`

If you use **[django-requests-api](https://pypi.org/project/django-requests-api/)** with django-iubenda, add a separate **`APP_CONFIG["requests_api"]`** block next to **`iubenda`**. That package reads **`CACHED_CLIENTS_MAXSIZE`**, **`DEFAULT_REQUEST_TIMEOUT`**, and top-level **`REQUESTS_API_*`** via **`requests_api.conf`**. Timeouts for Iubenda policy HTTP calls still come only from **`iubenda.conf`** (`IUBENDA_API_TIMEOUT` / `API_TIMEOUT`). See django-requests-api’s own docs under *Configuration*.

## Context processor and views

- **`iubenda.context_processors.iubenda`** uses `get_iubenda_options`, `get_iubenda_gtm`, `get_iubenda_csp_nonce`, `get_iubenda_autoblocking`.
- **Privacy/cookie views** use `get_iubenda_api_*`, `get_iubenda_use_compress` via `iubenda.api` / `iubenda.views`.

See also [HTTP client & policy API](http-api.md) for how API settings affect outbound requests.
