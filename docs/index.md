Django's application for handling privacy and cookie policies configured with Iubenda.

---

## Requirements

These packages are required:

-   Python +3.8 supported.
-   Django +3.2 supported.

We **highly recommend** and only officially support the latest patch release of each Python and Django series.


## Installation

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

To personalize the Iubenda script's behaviour, the dict `IUBENDA_OPTIONS` can be configured inside `settings.py`
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

### Integration with Google Tag Manager
If Google Tag Manager is implemented in your application and all needed settings were configured inside the container,
the variable `IUBENDA_GTM` can be set with the value `True` and the Iubenda's callback will be inserted inside the script.

For needed configuration inside Google Tag Manager container, please refer to these notes:
* [Google Consent Mode](https://www.iubenda.com/en/help/27137-google-consent-mode)
* [Google Consent Mode setup GTM with Iubenda](https://www.iubenda.com/en/help/74198-google-consent-mode-set-up-google-tag-manager-with-iubenda)
* [GTM Blocking Cookies](https://www.iubenda.com/en/help/1235-google-tag-manager-blocking-cookies)

## Example

Let's take a look at a quick example of using this project to build a simple App with **custom error pages**.

* Check the demo repo on [GitHub][github-demo]

## Quickstart

Can't wait to get started? The [quickstart guide][quickstart] is the fastest way to get up and running and building a **demo App**.

## Customize

Do you want custom solutions? The [customize][customize] section is an overview of which part are easy to design.
If you find how to personalize different scenarios or behaviors, a [pull request][pull-request] is welcome!

## Development

See the [Contribution guidelines][contributing] for information on how to clone  the repository, run the test suite and contribute changes back to django-iubenda.

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

[quickstart]: tutorial/example.md

[contributing]: community/contributing.md
[pull-request]: community/contributing.png#pull-request

[security-mail]: mailto:dlrsp.issue@gmail.com
