# -*- coding: utf-8 -*-
from bok_choy.page_object import PageObject


class state5Page(PageObject):
    """state5页"""
    url = "http://localhost:3000/#!/welcome"
    def clickAddOwnerLink(self):
        self.q(css="a.btn.btn-default").click()
    def clickErrorLink(self):
        self.q(css="a[title&#x3D;&#x27;trigger a RuntimeException to see how it is handled&#x27;]").click()
    def clickFindOwnerButton(self):
        self.q(css="button.btn.btn-default").click()
    def clickFindOwnersLink(self):
        self.q(css="a[title&#x3D;&#x27;find owners&#x27;]").click()
    def clickHomeLink(self):
        self.q(css="a[title&#x3D;&#x27;home page&#x27;]").click()
    def clickToggleNavigationButton(self):
        self.q(css="button.navbar-toggle").click()
    def clickVeterinariansLink(self):
        self.q(css="a[title&#x3D;&#x27;veterinarians&#x27;]").click()
    def fill(self):
         setLastNameTextField()
    def fillAndSubmit(self):
        self.fill()
        self.submit()
    def setLastNameTextField(self):
        setLastNameTextField(data.get("LAST_NAME"))
    def setLastNameTextField(self,lastNameValue):
        self.q(id="lastName").fill(lastNameValue)
    def submit(self):
        self.clickFindOwnerButton()
    def verifyPageLoaded(self):
        pass
    def verifyPageUrl(self):
        pass


