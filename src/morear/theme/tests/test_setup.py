# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from morear.theme.testing import MOREAR_THEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that morear.theme is properly installed."""

    layer = MOREAR_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if morear.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'morear.theme'))

    def test_browserlayer(self):
        """Test that IMorearThemeLayer is registered."""
        from morear.theme.interfaces import (
            IMorearThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IMorearThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MOREAR_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['morear.theme'])

    def test_product_uninstalled(self):
        """Test if morear.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'morear.theme'))

    def test_browserlayer_removed(self):
        """Test that IMorearThemeLayer is removed."""
        from morear.theme.interfaces import \
            IMorearThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMorearThemeLayer, utils.registered_layers())
