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

    def test_countryDetection(self):
        """Test default option's value: countryDetection"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"countryDetection": true')

    def test_askConsentAtCookiePolicyUpdate(self):
        """Test default option's value: askConsentAtCookiePolicyUpdate"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"askConsentAtCookiePolicyUpdate": true')

    def test_enableFadp(self):
        """Test default option's value: enableFadp"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"enableFadp": true')

    def test_enableLgpd(self):
        """Test default option's value: enableLgpd"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"enableLgpd": true')

    def test_lgpdAppliesGlobally(self):
        """Test default option's value: lgpdAppliesGlobally"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"lgpdAppliesGlobally": false')

    def test_enableUspr(self):
        """Test default option's value: lgpdAppliesGlobally"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"enableUspr": true')

    def test_enableCcpa(self):
        """Test default option's value: enableCcpa"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"enableCcpa": true')

    def test_ccpaAcknowledgeOnDisplay(self):
        """Test default option's value: ccpaAcknowledgeOnDisplay"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"ccpaAcknowledgeOnDisplay": true')

    def test_ccpaApplies(self):
        """Test default option's value: ccpaApplies"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"ccpaApplies": true')

    def test_consentOnContinuedBrowsing(self):
        """Test default option's value: consentOnContinuedBrowsing"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"consentOnContinuedBrowsing": false')

    def test_floatingPreferencesButtonDisplay(self):
        """Test default option's value: floatingPreferencesButtonDisplay"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(
            response, '"floatingPreferencesButtonDisplay": "bottom-left"'
        )

    def test_invalidateConsentWithoutLog(self):
        """Test default option's value: invalidateConsentWithoutLog"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"invalidateConsentWithoutLog": true')

    def test_perPurposeConsent(self):
        """Test default option's value: perPurposeConsent"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"perPurposeConsent": true')

    def test_whitelabel(self):
        """Test default option's value: whitelabel"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"whitelabel": false')
