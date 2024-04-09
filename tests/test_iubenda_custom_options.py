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

    @override_settings(IUBENDA_OPTIONS={"countryDetection": "false"})
    def test_countryDetection(self):
        """Test custom option's value: countryDetection"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"countryDetection": false')

    @override_settings(IUBENDA_OPTIONS={"askConsentAtCookiePolicyUpdate": "false"})
    def test_askConsentAtCookiePolicyUpdate(self):
        """Test custom option's value: askConsentAtCookiePolicyUpdate"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"askConsentAtCookiePolicyUpdate": false')

    @override_settings(IUBENDA_OPTIONS={"enableFadp": "false"})
    def test_enableFadp(self):
        """Test custom option's value: enableFadp"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"enableFadp": false')

    @override_settings(IUBENDA_OPTIONS={"enableLgpd": "false"})
    def test_enableLgpd(self):
        """Test custom option's value: enableLgpd"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"enableLgpd": false')

    @override_settings(IUBENDA_OPTIONS={"lgpdAppliesGlobally": "false"})
    def test_lgpdAppliesGlobally(self):
        """Test custom option's value: lgpdAppliesGlobally"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"lgpdAppliesGlobally": false')

    @override_settings(IUBENDA_OPTIONS={"enableUspr": "false"})
    def test_enableUspr(self):
        """Test custom option's value: lgpdAppliesGlobally"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"enableUspr": false')

    @override_settings(IUBENDA_OPTIONS={"enableCcpa": "false"})
    def test_enableCcpa(self):
        """Test custom option's value: enableCcpa"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"enableCcpa": false')

    @override_settings(IUBENDA_OPTIONS={"ccpaAcknowledgeOnDisplay": "false"})
    def test_ccpaAcknowledgeOnDisplay(self):
        """Test custom option's value: ccpaAcknowledgeOnDisplay"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"ccpaAcknowledgeOnDisplay": false')

    @override_settings(IUBENDA_OPTIONS={"ccpaApplies": "false"})
    def test_ccpaApplies(self):
        """Test custom option's value: ccpaApplies"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"ccpaApplies": false')

    @override_settings(IUBENDA_OPTIONS={"consentOnContinuedBrowsing": "true"})
    def test_consentOnContinuedBrowsing(self):
        """Test custom option's value: consentOnContinuedBrowsing"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"consentOnContinuedBrowsing": true')

    @override_settings(
        IUBENDA_OPTIONS={"floatingPreferencesButtonDisplay": "bottom-right"}
    )
    def test_floatingPreferencesButtonDisplay(self):
        """Test custom option's value: floatingPreferencesButtonDisplay"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(
            response, '"floatingPreferencesButtonDisplay": "bottom-right"'
        )

    @override_settings(IUBENDA_OPTIONS={"invalidateConsentWithoutLog": "false"})
    def test_invalidateConsentWithoutLog(self):
        """Test custom option's value: invalidateConsentWithoutLog"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"invalidateConsentWithoutLog": false')

    @override_settings(IUBENDA_OPTIONS={"perPurposeConsent": "false"})
    def test_perPurposeConsent(self):
        """Test custom option's value: perPurposeConsent"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"perPurposeConsent": false')

    @override_settings(IUBENDA_OPTIONS={"whitelabel": "true"})
    def test_whitelabel(self):
        """Test custom option's value: whitelabel"""
        LOGGER.debug("Tests tearDown")
        response = self.client.get("/privacy-policy/", follow=True)
        LOGGER.debug(response)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '"whitelabel": true')
