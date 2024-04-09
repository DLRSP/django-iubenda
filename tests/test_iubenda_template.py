"""Unit Tests for the module"""

import logging

from django.test import TransactionTestCase, override_settings

LOGGER = logging.getLogger(name="django-iubenda")


class IubendaTestCase(TransactionTestCase):
    """Test Case for django-iubenda"""

    fixtures = ["data.json"]

    def setUp(self):
        """Set up common assets for tests"""
        LOGGER.debug("Tests setUp")

    def tearDown(self):
        """Remove Test Data"""
        LOGGER.debug("Tests tearDown")

    def test_privacy_template_with_compress(self):
        """Test that render Privacy page using compress."""
        LOGGER.debug("Render Compressed Privacy page")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "iubenda/privacy-compress.html")

    def test_cookie_template_with_compress(self):
        """Test that render Cookie page using compress."""
        LOGGER.debug("Render Compressed Cookie page")
        response = self.client.get("/cookie-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "iubenda/cookie-compress.html")

    @override_settings(IUBENDA_USE_COMPRESS=False)
    def test_privacy_template(self):
        """Test that render Privacy page."""
        LOGGER.debug("Render Privacy page")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "iubenda/privacy.html")

    @override_settings(IUBENDA_USE_COMPRESS=False)
    def test_cookie_template(self):
        """Test that render Cookie page."""
        LOGGER.debug("Render Cookie page")
        response = self.client.get("/cookie-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "iubenda/cookie.html")
