Django's application for handling privacy and cookie policies configured with Iubenda.

---

## Requirements

These packages are required:

-   Python 3.8 or newer.
-   Django 3.2 or newer (see package metadata for supported releases).
-   **django-requests-api** — shared HTTP client package (`requests_api`). Typical import: `from requests_api import RequestsApi, normalize_api_language, copy_get_params_with_overrides, requests_api_for_base`.

We run CI against current patch releases of the supported Python and Django versions.


## Installation

1. Install from **pip**:
```shell
pip install django-iubenda
```

2. Modify `settings.py` by adding the apps to `INSTALLED_APPS` (same pattern as other projects using **django-requests-api**):
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

9. Modify your project's template to add privacy and cookie policies.
   For example inside the `footer.html` add following code:
```html
{% if not debug %}
    {% block iubenda %}{% include "iubenda/include-content.html" %}{% endblock iubenda %}
{% endif %}
```

## Configuration (`APP_CONFIG` and `IUBENDA_*`)

Runtime options are resolved in **`iubenda.conf`** (same pattern as apps such as **copyai**):

1. Top-level **`IUBENDA_*`** settings (for strings, empty values are skipped so the next layer can apply).
2. **`APP_CONFIG["iubenda"]`** — short keys: `API_BASE_URL`, `API_ALLOWED_LANGS`, `API_FALLBACK_LANG`, `API_TIMEOUT`, `USE_COMPRESS`, `OPTIONS`, `GTM`, `CSP_NONCE`, `AUTOBLOCKING`.
3. Defaults in **`iubenda.defaults`**.

Full table and examples: [Configuration tutorial](tutorial/configuration.md). If you use **django-requests-api**, optional **`APP_CONFIG["requests_api"]`** is separate and documented in that package; Iubenda API timeouts remain under **`iubenda.conf`**.

## Optional

### Autoblocking
If Iubenda autoblocking's configurations are implemented in your account,
set `IUBENDA_AUTOBLOCKING = True` or `APP_CONFIG["iubenda"]["AUTOBLOCKING"] = True` to load the autoblocking script.
```html
<script src="https://cs.iubenda.com/autoblocking/{{ cx_iubenda.iub_site_id }}.js"></script>
```

### Privacy and cookie API requests

The privacy and cookie views load policy content from Iubenda’s HTTP API. The **`lang`** query parameter is derived from `request.LANGUAGE_CODE` using your allowed-language settings; other GET parameters are merged in a controlled way so the API receives a consistent `lang` for your published policies. Values come from **`iubenda.conf`** (`IUBENDA_API_*` and/or `APP_CONFIG["iubenda"]`).

| Setting | `APP_CONFIG["iubenda"]` key | Role |
|--------|-----------------------------|------|
| `IUBENDA_API_BASE_URL` | `API_BASE_URL` | Base URL for API calls (default: `https://www.iubenda.com`). |
| `IUBENDA_API_ALLOWED_LANGS` | `API_ALLOWED_LANGS` | Allowed `lang` values (default: `it`, `en`). |
| `IUBENDA_API_FALLBACK_LANG` | `API_FALLBACK_LANG` | Fallback when the active language is not allowed (default: `en`). |
| `IUBENDA_API_TIMEOUT` | `API_TIMEOUT` | Per-request timeout in seconds (default: `30`). |

**Imports**

- This app: `iubenda.api` — `normalize_iubenda_lang`, `iubenda_request_params`, `get_iubenda_client`, `api_request_timeout` (all use `iubenda.conf`).
- django-requests-api: `from requests_api import normalize_api_language, copy_get_params_with_overrides, requests_api_for_base, RequestsApi`.

More detail: [HTTP client & policy API](tutorial/http-api.md).

### Content Security Policy

If you use a **Content Security Policy** and block inline scripts unless they carry a nonce, set **`IUBENDA_CSP_NONCE`** or **`APP_CONFIG["iubenda"]["CSP_NONCE"]`** so django-iubenda can render script tags with a `nonce` attribute. Your web server or middleware must issue a fresh nonce per response and expose it to templates the same way you do for other inline scripts.

Example template snippet:

```html
<script {% if cx_iubenda_nonce %}nonce="{{ cx_iubenda_nonce }}"{% endif %}>
```

You still need to allow Iubenda hosts in the relevant CSP directives (`script-src`, `connect-src`, `img-src`, `style-src`, `frame-src`, etc.). Exact values depend on your setup; start from Iubenda’s guide and your browser console errors.

If you avoid `'unsafe-inline'`, you may need to add **hash** sources for specific inline snippets—the console usually prints the values to use.

See Iubenda’s English guide: [How to configure Content Security Policy for iubenda](https://www.iubenda.com/en/help/12260-how-to-configure-content-security-policy-to-allow-iubenda-scripts-to-execute).

### Iubenda options

To customize the Iubenda script, set **`IUBENDA_OPTIONS`** (or **`APP_CONFIG["iubenda"]["OPTIONS"]`**) in `settings.py`:

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
set `IUBENDA_GTM = True` or `APP_CONFIG["iubenda"]["GTM"] = True` so the Iubenda callback is inserted into the script. See [Google Tag Manager](tutorial/google-gtm.md).

For needed configuration inside Google Tag Manager container, please refer to these notes:
* [Google Consent Mode](https://www.iubenda.com/en/help/27137-google-consent-mode)
* [Google Consent Mode setup GTM with Iubenda](https://www.iubenda.com/en/help/74198-google-consent-mode-set-up-google-tag-manager-with-iubenda)
* [GTM Blocking Cookies](https://www.iubenda.com/en/help/1235-google-tag-manager-blocking-cookies)

## Example

The [example project][github-demo] repository demonstrates django-iubenda integrated into a small Django site (privacy and cookie URLs, context processor, `requests_api` in `INSTALLED_APPS`).

Step-by-step clone and run: [Example project](tutorial/example.md).

## Quickstart

Use the [example project](tutorial/example.md) guide for the fastest path from clone to a running demo.

## Customize

Templates, HTTP/API usage, and Google Tag Manager are summarized in the [customize overview](tutorial/customize.md). Doc fixes are welcome via [pull requests][pull-request].

## Development

See the [Contribution guidelines][contributing] for how to clone the repository, run tests, and submit changes.

## Security

If you believe you’ve found something in this project which has security implications, please **do not raise the issue in a public forum**.

Send a description of the issue via email to [dlrsp.issue@gmail.com][security-mail].  The project maintainers will then work with you to resolve any issues where required, prior to any public disclosure.

## License

MIT License

Copyright (c) 2010-present DLRSP (https://dlrsp.org) and other contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[index]: .
[github-demo]: https://github.com/DLRSP/example/tree/django-iubenda

[contributing]: community/contributing.md
[pull-request]: community/contributing.md#pull-requests

[security-mail]: mailto:dlrsp.issue@gmail.com
