"""Tests for Iubenda API query helpers."""

from django.test import RequestFactory, SimpleTestCase, override_settings

from iubenda.api import (
    api_request_timeout,
    iubenda_request_params,
    normalize_iubenda_lang,
)
from iubenda.conf import get_iubenda_api_base_url


class NormalizeIubendaLangTests(SimpleTestCase):
    def test_primary_subtag(self):
        self.assertEqual(normalize_iubenda_lang("it-it"), "it")

    def test_zh_hans_falls_back_to_en(self):
        self.assertEqual(normalize_iubenda_lang("zh-hans"), "en")

    def test_none_uses_fallback(self):
        self.assertEqual(normalize_iubenda_lang(None), "en")

    @override_settings(IUBENDA_API_ALLOWED_LANGS=("de", "fr"), IUBENDA_API_FALLBACK_LANG="de")
    def test_custom_allowed_and_fallback(self):
        self.assertEqual(normalize_iubenda_lang("de-at"), "de")
        self.assertEqual(normalize_iubenda_lang("it"), "de")


class IubendaRequestParamsTests(SimpleTestCase):
    def test_lang_forced_from_language_code(self):
        rf = RequestFactory()
        request = rf.get("/privacy-policy/", {"lang": "zh-hans"})
        request.LANGUAGE_CODE = "zh-hans"
        params = iubenda_request_params(request)
        self.assertEqual(params["lang"], "en")

    def test_other_get_preserved(self):
        rf = RequestFactory()
        request = rf.get("/privacy-policy/", {"foo": "bar"})
        request.LANGUAGE_CODE = "it"
        params = iubenda_request_params(request)
        self.assertEqual(params["lang"], "it")
        self.assertEqual(params["foo"], "bar")


@override_settings(IUBENDA_API_TIMEOUT=12.5)
class ApiTimeoutTests(SimpleTestCase):
    def test_timeout_from_settings(self):
        self.assertEqual(api_request_timeout(), 12.5)


@override_settings(APP_CONFIG={"iubenda": {"API_TIMEOUT": 42.0}})
class AppConfigApiTests(SimpleTestCase):
    def test_timeout_from_app_config(self):
        self.assertEqual(api_request_timeout(), 42.0)


@override_settings(
    APP_CONFIG={"iubenda": {"API_ALLOWED_LANGS": ("de", "fr"), "API_FALLBACK_LANG": "de"}}
)
class AppConfigLangTests(SimpleTestCase):
    def test_allowed_langs_from_app_config(self):
        self.assertEqual(normalize_iubenda_lang("de-ch"), "de")
        self.assertEqual(normalize_iubenda_lang("it"), "de")


@override_settings(
    IUBENDA_API_BASE_URL="",
    APP_CONFIG={"iubenda": {"API_BASE_URL": "https://config.example.test"}},
)
class AppConfigBaseUrlTests(SimpleTestCase):
    def test_empty_top_level_string_uses_app_config(self):
        self.assertEqual(get_iubenda_api_base_url(), "https://config.example.test")


@override_settings(
    IUBENDA_API_BASE_URL="https://top.example",
    APP_CONFIG={"iubenda": {"API_BASE_URL": "https://ignored.example"}},
)
class TopLevelWinsTests(SimpleTestCase):
    def test_top_level_base_url_over_app_config(self):
        self.assertEqual(get_iubenda_api_base_url(), "https://top.example")
