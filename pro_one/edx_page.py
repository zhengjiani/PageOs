from bok_choy.page_object import PageObject

class EdxHomePage(PageObject):
    url = 'http://www.edx.org'

    def is_browser_on_page(self):
        return 'edx' in self.browser.title.lower()