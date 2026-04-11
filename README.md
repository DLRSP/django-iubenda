# django-iubenda [![PyPi license](https://img.shields.io/pypi/l/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)

[![PyPi status](https://img.shields.io/pypi/status/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)
[![PyPi version](https://img.shields.io/pypi/v/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)
[![PyPi python version](https://img.shields.io/pypi/pyversions/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)
[![PyPi downloads](https://img.shields.io/pypi/dm/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)
[![PyPi downloads](https://img.shields.io/pypi/dw/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)
[![PyPi downloads](https://img.shields.io/pypi/dd/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)

## GitHub ![GitHub release](https://img.shields.io/github/tag/DLRSP/django-iubenda.svg) ![GitHub release](https://img.shields.io/github/release/DLRSP/django-iubenda.svg)

## Test [![codecov.io](https://codecov.io/github/DLRSP/django-iubenda/coverage.svg?branch=main)](https://codecov.io/github/DLRSP/django-iubenda?branch=main) [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/DLRSP/django-iubenda/main.svg)](https://results.pre-commit.ci/latest/github/DLRSP/django-iubenda/main) [![CI](https://github.com/DLRSP/django-iubenda/actions/workflows/ci.yaml/badge.svg)](https://github.com/DLRSP/django-iubenda/actions/workflows/ci.yaml)

## Compliance for websites and apps
Click [here](http://iubenda.refr.cc/dlrspapi) and get 10% discount on first year at Iubenda
[![Iubenda](https://client-assets.referralcandy.com/md6Y46jBT5ufTCO2zzGt_1668598186.png)](http://iubenda.refr.cc/dlrspapi)


## Check Demo Project
* Check the demo repo on [GitHub](https://github.com/DLRSP/example/tree/django-iubenda)

## Requirements
-   Python 3.8 or newer.
-   Django 3.2 or newer (see package metadata for supported releases).
-   **django-requests-api** (`requests_api`) — shared HTTP client; typical import: `from requests_api import RequestsApi, normalize_api_language, copy_get_params_with_overrides, requests_api_for_base`.

## Setup
1. Install from **pip**:
   ```shell
   pip install django-iubenda
   ```
2. Modify `settings.py` by adding the apps to `INSTALLED_APPS` (same pattern as other DLRSP integrations that use **django-requests-api**):
   ```python
   INSTALLED_APPS = (
       "modeltranslation",
       # ...
       "requests_api",
       "iubenda",
       # ...
   )
   ```
3. Modify `settings.py` by adding the app's context processor to `TEMPLATES`:
   ```python
   TEMPLATES = [
       {
           # ...
           "OPTIONS": {
               "context_processors": [
                   # ...
                   "iubenda.context_processors.iubenda",
                   # ...
               ],
           },
       },
   ]
   ```
4. Be sure the Django's Locale middleware is enabled inside `settings.py`:
   ```python
   MIDDLEWARE = (
       # ...
       "django.middleware.locale.LocaleMiddleware",
       # ...
   )
   ```
5. Optionally, enable Django’s **CurrentSiteMiddleware** in `settings.py`:
   ```python
   MIDDLEWARE = (
       # ...
       "django.contrib.sites.middleware.CurrentSiteMiddleware",
       # ...
   )
   ```
6. In `urls.py`, include the app’s URLconf:
   ```python
   urlpatterns += [
       path("", include("iubenda.urls")),
   ]
   ```
7. Register the app’s sitemaps (for example in `urls.py` or wherever you define `sitemaps`):
   ```python
   from iubenda.sitemaps import PrivacySitemap, CookieSitemap

   sitemaps = {
       # ...
       "privacy": PrivacySitemap,
       "cookie": CookieSitemap,
       # ...
   }
   ```
8. Be sure the variable `LANGUAGE_CODE` is available for HTML templates:
   ```html
   {% load i18n %}
   {% get_current_language as LANGUAGE_CODE %}
   ```
9. In your base layout or footer template, include the Iubenda fragment—for example in `footer.html`:
   ```html
   {% if not debug %}
       {% block iubenda %}{% include "iubenda/include-content.html" %}{% endblock iubenda %}
   {% endif %}
   ```

## Configuration (`APP_CONFIG` and `IUBENDA_*`)

Options are resolved in **`iubenda.conf`**, consistent with other DLRSP apps (for example **copyai**):

1. Top-level **`IUBENDA_*`** (empty strings are skipped for string settings so the next source can apply).
2. **`APP_CONFIG["iubenda"]`** — keys such as `API_BASE_URL`, `API_ALLOWED_LANGS`, `API_FALLBACK_LANG`, `API_TIMEOUT`, `USE_COMPRESS`, `OPTIONS`, `GTM`, `CSP_NONCE`, `AUTOBLOCKING`.
3. Defaults in **`iubenda.defaults`**.

```python
APP_CONFIG = {
    "iubenda": {
        "API_TIMEOUT": 45,
        "GTM": True,
        "OPTIONS": {"perPurposeConsent": "true"},
    },
}
```

Full reference: `docs/tutorial/configuration.md` (MkDocs: *Tutorials → Configuration (APP_CONFIG)*). Optional **`APP_CONFIG["requests_api"]`** for django-requests-api is documented in that package; django-iubenda policy API timeouts stay under **`iubenda.conf`** (`IUBENDA_API_TIMEOUT` / `API_TIMEOUT`).

## Optional

### Autoblocking
If Iubenda autoblocking's configurations are implemented in your account,
set `IUBENDA_AUTOBLOCKING` or `APP_CONFIG["iubenda"]["AUTOBLOCKING"]` to enable the script.
```html
<script src="https://cs.iubenda.com/autoblocking/{{ cx_iubenda.iub_site_id }}.js"></script>
```

### Privacy and cookie API requests
The privacy and cookie views call Iubenda’s HTTP API with a **`lang`** query parameter aligned to `request.LANGUAGE_CODE` and to the languages your policies support. Values are read via **`iubenda.conf`** (`IUBENDA_API_*` and/or `APP_CONFIG["iubenda"]` keys `API_BASE_URL`, `API_ALLOWED_LANGS`, `API_FALLBACK_LANG`, `API_TIMEOUT`).

- `IUBENDA_API_BASE_URL` / `API_BASE_URL` — base URL for API calls (default: `https://www.iubenda.com`).
- `IUBENDA_API_ALLOWED_LANGS` / `API_ALLOWED_LANGS` — allowed `lang` values (default: `it`, `en`).
- `IUBENDA_API_FALLBACK_LANG` / `API_FALLBACK_LANG` — used when the active language is not allowed (default: `en`).
- `IUBENDA_API_TIMEOUT` / `API_TIMEOUT` — seconds for API HTTP calls (default: `30`).

Use `iubenda.api` for Iubenda-specific helpers (they use `iubenda.conf`), or `from requests_api import …` for the shared client. Tutorials: `docs/tutorial/http-api.md`, `docs/tutorial/configuration.md`.

### Content Security Policy

If you use a **Content Security Policy** and block inline scripts unless they carry a nonce, set **`IUBENDA_CSP_NONCE`** or **`APP_CONFIG["iubenda"]["CSP_NONCE"]`** so django-iubenda can render script tags with a `nonce` attribute. Your server or middleware must issue a fresh nonce per response and pass it into templates like your other inline scripts.

```html
<script {% if cx_iubenda_nonce %}nonce="{{ cx_iubenda_nonce }}"{% endif %}>
```

Allow Iubenda hosts in the relevant CSP directives (`script-src`, `connect-src`, `img-src`, `style-src`, `frame-src`, etc.). Details depend on your stack; use Iubenda’s guide and your browser console. If you avoid `'unsafe-inline'`, you may need hash sources for specific snippets.

[Iubenda: Content Security Policy and iubenda scripts](https://www.iubenda.com/en/help/12260-how-to-configure-content-security-policy-to-allow-iubenda-scripts-to-execute)

### Iubenda options

Set **`IUBENDA_OPTIONS`** or **`APP_CONFIG["iubenda"]["OPTIONS"]`** in `settings.py`:
```python
IUBENDA_OPTIONS = {
    "countryDetection": "true",
    "askConsentAtCookiePolicyUpdate": "true",
    "enableFadp": "true",
    "enableLgpd": "true",
    "lgpdAppliesGlobally": "true",
    "enableUspr": "true",
    "enableCcpa": "true",
    "ccpaAcknowledgeOnDisplay": "true",
    "ccpaApplies": "true",
    "consentOnContinuedBrowsing": "false",
    "floatingPreferencesButtonDisplay": "bottom-left",
    "invalidateConsentWithoutLog": "true",
    "perPurposeConsent": "true",
    "whitelabel": "false",
    "banner": {
        "acceptButtonDisplay": "true",
        "backgroundOverlay": "true",
        "closeButtonRejects": "true",
        "customizeButtonDisplay": "true",
        "explicitWithdrawal": "true",
        "fontSize": "14px",
        "listPurposes": "true",
        "position": "float-center",
        "rejectButtonDisplay": "true",
        "showPurposesToggles": "true",
    },
}
```

### Integration with Google Tag Manager
If Google Tag Manager is implemented in your application and all needed settings were configured inside the container,
set `IUBENDA_GTM = True` or `APP_CONFIG["iubenda"]["GTM"] = True` so the Iubenda callback is inserted into the script.

For needed configuration inside Google Tag Manager container, please refer to these notes:
- [Google Consent Mode](https://www.iubenda.com/en/help/27137-google-consent-mode)
- [Google Consent Mode setup GTM with Iubenda](https://www.iubenda.com/en/help/74198-google-consent-mode-set-up-google-tag-manager-with-iubenda)
- [GTM Blocking Cookies](https://www.iubenda.com/en/help/1235-google-tag-manager-blocking-cookies)

## Run Example Project

```shell
git clone --depth=50 --branch=django-iubenda https://github.com/DLRSP/example.git DLRSP/example
cd DLRSP/example
python manage.py runserver
```

Now browser the app @ http://127.0.0.1:8000
