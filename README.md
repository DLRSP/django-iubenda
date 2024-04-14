# django-iubenda [![PyPi license](https://img.shields.io/pypi/l/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)

[![PyPi status](https://img.shields.io/pypi/status/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)
[![PyPi version](https://img.shields.io/pypi/v/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)
[![PyPi python version](https://img.shields.io/pypi/pyversions/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)
[![PyPi downloads](https://img.shields.io/pypi/dm/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)
[![PyPi downloads](https://img.shields.io/pypi/dw/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)
[![PyPi downloads](https://img.shields.io/pypi/dd/django-iubenda.svg)](https://pypi.python.org/pypi/django-iubenda)

## GitHub ![GitHub release](https://img.shields.io/github/tag/DLRSP/django-iubenda.svg) ![GitHub release](https://img.shields.io/github/release/DLRSP/django-iubenda.svg)

## Test [![codecov.io](https://codecov.io/github/DLRSP/django-iubenda/coverage.svg?branch=main)](https://codecov.io/github/DLRSP/django-iubenda?branch=main) [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/DLRSP/django-iubenda/main.svg)](https://results.pre-commit.ci/latest/github/DLRSP/django-iubenda/main) [![gitthub.com](https://github.com/DLRSP/django-iubenda/actions/workflows/ci.yaml/badge.svg)](https://github.com/DLRSP/django-iubenda/actions/workflows/ci.yaml)

## Compliance for websites and apps
Click [here](http://iubenda.refr.cc/dlrspapi) and get 10% discount on first year at Iubenda
[![Iubenda](https://client-assets.referralcandy.com/md6Y46jBT5ufTCO2zzGt_1668598186.png)](http://iubenda.refr.cc/dlrspapi)


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
5. Optionally, but sugguested, the Django's Current Site middleware is enabled inside `settings.py`:
   ```python
   MIDDLEWARE = (
       # ...
       "django.contrib.sites.middleware.CurrentSiteMiddleware",
       # ...
   )
   ```
6. Modify `url.py` by adding the app's urls to `urlpatterns`:
   ```python
   urlpatterns += [
       path("", include("iubenda.urls")),
   ]
   ```
7. Modify `url.py` by adding the app's sitemaps to `sitemaps`:
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

## Optional

### Autoblocking
If Iubenda autoblocking's configurations are implemented in your account,
the variable `IUBENDA_AUTOBLOCKING` can be set to import the site's script.
```html
<script src="https://cs.iubenda.com/autoblocking/{{ cx_iubenda.iub_site_id }}.js"></script>
```

### Content Security Policy
If Content Security Policy are implemented in your server and inline scripts are disabled,
the variable `IUBENDA_CSP_NONCE` can be set with nonce tag will be inserted script's nonce.
```html
<script {% if cx_iubenda_nonce %}nonce="{{ cx_iubenda_nonce }}"{% endif %}>
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

To personalize the Iubenda script's behaviour, the dict `IUBENDA_OPTIONS` can be configured inside `settings.py`
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
the variable `IUBENDA_GTM` can be set with the value `True` and the Iubenda's callback will be inserted inside the script.

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
