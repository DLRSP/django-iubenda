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

    def test_default_nonce(self):
        """Remove Test Data"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertNotContains(response, "nonce")

    @override_settings(IUBENDA_CSP_NONCE=None)
    def test_without_nonce(self):
        """Remove Test Data"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertNotContains(response, "nonce")

    @override_settings(IUBENDA_CSP_NONCE="CUSTOM_NONCE_OVERRIDE")
    def test_nonce(self):
        """Remove Test Data"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "CUSTOM_NONCE_OVERRIDE")

    def test_default_gtm(self):
        """Remove Test Data"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertNotContains(response, "googleConsentMode")

    @override_settings(IUBENDA_GTM=True)
    def test_gtm(self):
        """Remove Test Data"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "googleConsentMode")

    @override_settings(IUBENDA_GTM=False)
    def test_without_gtm(self):
        """Remove Test Data"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertNotContains(response, "googleConsentMode")

    def test_default_autoblocking(self):
        """Remove Test Data"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertNotContains(response, "autoblocking")

    @override_settings(IUBENDA_AUTOBLOCKING=False)
    def test_without_autoblocking(self):
        """Remove Test Data"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertNotContains(response, "autoblocking")

    @override_settings(IUBENDA_AUTOBLOCKING=True)
    def test_autoblocking(self):
        """Remove Test Data"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertNotContains(response, "autoblocking")
