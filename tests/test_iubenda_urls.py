"""Unit Tests for the module"""

import logging

from django.test import TransactionTestCase

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

    def test_sitemap(self):
        """Test that render sitemap.xml."""
        LOGGER.debug("Render Sitemap")
        response = self.client.get("/it/sitemap.xml", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)

    def test_privacy_urls(self):
        """Test that render Privacy page."""
        LOGGER.debug("Render Privacy page")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)

    def test_cookie_urls(self):
        """Test that render Cookie page."""
        LOGGER.debug("Render Cookie page")
        response = self.client.get("/cookie-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
