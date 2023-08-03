# django-iubenda [![PyPi license](https://img.shields.io/pypi/l/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)

[![PyPi status](https://img.shields.io/pypi/status/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)
[![PyPi version](https://img.shields.io/pypi/v/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)
[![PyPi python version](https://img.shields.io/pypi/pyversions/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)
[![PyPi downloads](https://img.shields.io/pypi/dm/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)
[![PyPi downloads](https://img.shields.io/pypi/dw/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)
[![PyPi downloads](https://img.shields.io/pypi/dd/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)

## GitHub ![GitHub release](https://img.shields.io/github/tag/DLRSP/django-iubenda.svg) ![GitHub release](https://img.shields.io/github/release/DLRSP/django-iubenda.svg)

## Test [![codecov.io](https://codecov.io/github/DLRSP/django-iubenda/coverage.svg?branch=master)](https://codecov.io/github/DLRSP/django-iubenda?branch=master) [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/DLRSP/django-iubenda/master.svg)](https://results.pre-commit.ci/latest/github/DLRSP/django-iubenda/master) [![gitthub.com](https://github.com/DLRSP/django-iubenda/actions/workflows/ci.yml/badge.svg)](https://github.com/DLRSP/django-iubenda/actions/workflows/ci.yml)

## Compliance for websites and apps
Click [here](http://iubenda.refr.cc/dlrspapi) and get 10% discount on first year at Iubenda
[![Iubenda](https://cdn.filestackcontent.com/kTEmy2XBQJiiEy0ULvg0)](http://iubenda.refr.cc/dlrspapi)


## Check Demo Project
* Check the demo repo on [GitHub](https://github.com/DLRSP/example/tree/django-iubenda)

## Requirements
-   Python +3.8 supported.
-   Django +3.2 supported.

## Setup
1. Install from **pip**:
```shell
pip install django-iubenda
```

2. Modify `settings.py` by adding the app to `INSTALLED_APPS`:
```python
INSTALLED_APPS = (
    "modeltranslation",
    # ...
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

5. Modify `url.py` by adding the app's urls to `urlpatterns`:
```python
urlpatterns += [
    path("", include("iubenda.urls")),
]
```

6. Modify `url.py` by adding the app's sitemaps to `sitemaps`:
```python
from iubenda.sitemaps import PrivacySitemap, CookieSitemap

sitemaps = {
    # ...
    "privacy": PrivacySitemap,
    "cookie": CookieSitemap,
    # ...
}
```

7. Be sure the variable `LANGUAGE_CODE` is available for HTML templates:
```html
{% load i18n %}
{% get_current_language as LANGUAGE_CODE %}
```

8. Modify your project's template to add privacy and cookie policies.
   For example inside the `footer.html` add following code:
```html
{% if not debug %}
    {% block iubenda %}{% include "iubenda/include-content.html" %}{% endblock iubenda %}
{% endif %}
```

## Optional

### Content Security Policy
If Content Security Policy are implemented in your server and inline scripts are disabled,
the variable `IUBENDA_CSP_NONCE` can be set with nonce tag will be inserted script's nonce.
```html
<script type="text/javascript" {% if cx_iubenda_nonce %}nonce="{{ cx_iubenda_nonce }}"{% endif %}>
```
Inside your webserver's configurations, a rule to dynamically replace your CONSTANT nonce in a random string is needed.

To allow  external source from Iubenda domains, please implement these rules:
```editorconfig
Content-Security-Policy:
    script-src-elem https://*.iubenda.com";
    img-src https://*.iubenda.com data:";
    style-src https://*.iubenda.com";
    connect-src https://*.iubenda.com";
    frame-src https://*.iubenda.com";
```

If you prefer to not allow ***unsafe-inline*** inside your CSP, please also add the two specific hash for your
script prompted as error in Javascript Console.
```editorconfig
# Iubenda Privacy And Cookie Policy - API
Content-Security-Policy:
    ...
    script-src-elem https://*.iubenda.com 'sha256-YOUR-FIRST-HASH-PROMPTED-INSIDE-CONSOLE' 'sha256-YOUR-SECOND-HASH-PROMPTED-INSIDE-CONSOLE';
    ...
```

Check this article from [Iubenda help](https://www.iubenda.com/it/help/12347-come-configurare-il-content-security-policy-per-consentire-lesecuzione-degli-script-di-iubenda)

### Iubenda's Options
(To-Do: new feuture)

To personalize the Iubenda script behaviour, the dict `IUBENDA_OPTIONS` can be configured inside `settings.py`
```python
IUBENDA_OPTIONS = {
    "ccpaAcknowledgeOnDisplay": "true",
    "ccpaApplies": "true",
    "consentOnContinuedBrowsing": "false",
    "enableCcpa": "true",
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
    },
}
```

## Run Example Project

```shell
git clone --depth=50 --branch=django-iubenda https://github.com/DLRSP/example.git DLRSP/example
cd DLRSP/example
python manage.py runserver
```

Now browser the app @ http://127.0.0.1:8000
