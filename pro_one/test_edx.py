from bok_choy.web_app_test import WebAppTest
from pro_one.edx_page import EdxHomePage

class TestEdxHomePage(WebAppTest):

    def test_page_existence(self):
        homepage=EdxHomePage(self.browser).visit()
        css_locator = 'img.site-logo'
        self.assertTrue(homepage.q(css=css_locator).first.visible)
        self.assertScreenshot(css_locator, 'edx_logo_header')