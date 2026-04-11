# Google Tag Manager

If you use Google Tag Manager and have configured your container for Iubenda, you can let django-iubenda inject the consent callback expected by that setup.

## Setting

Either a top-level flag or `APP_CONFIG` (see [Configuration](configuration.md)):

```python
IUBENDA_GTM = True
```

```python
APP_CONFIG = {
    "iubenda": {"GTM": True},
}
```

Ensure the rest of your Iubenda integration (site ID, options, etc.) is configured as in the main [documentation](../index.md#optional).

## Iubenda guides

- [Google Consent Mode](https://www.iubenda.com/en/help/27137-google-consent-mode)
- [Google Consent Mode and GTM with Iubenda](https://www.iubenda.com/en/help/74198-google-consent-mode-set-up-google-tag-manager-with-iubenda)
- [GTM and cookie blocking](https://www.iubenda.com/en/help/1235-google-tag-manager-blocking-cookies)
