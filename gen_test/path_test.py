import unittest
from bok_choy.web_app_test import WebAppTest
from bokchoy_pages.pet_page import EditOwnerPage,HomePage,AddNewVisitPage,PetPage,DetailPage,RegisterPage,FindPage,VeterPage


class Test(WebAppTest):
    
    def test_path1(self):
        self.homepage = HomePage(self.browser)
        self.findpage = FindPage(self.browser)
        
        self.detailpage = DetailPage(self.browser)
        self.homepage.goto_search()
        
        self.findpage.goto_detail_page()
        
    def test_path2(self):
        self.homepage = HomePage(self.browser)
        self.findpage = FindPage(self.browser)
        
        self.detailpage = DetailPage(self.browser)
        self.homepage.goto_search()
        
        self.findpage.goto_detail_page()
        
        self.detailpage.goto_edit_pet()
        self.petpage.edit_pet(R1)
        
    def test_path3(self):
        self.homepage = HomePage(self.browser)
        self.findpage = FindPage(self.browser)
        self.detailpage = DetailPage(self.browser)
        self.petpage = PetPage(self.browser)
        
        self.detailpage = DetailPage(self.browser)
        self.homepage.goto_search()
        
        self.findpage.goto_detail_page()
        
        self.detailpage.goto_visit()
        self.addnewvisitpage.add_visit(R1)
        
    def test_path4(self):
        self.homepage = HomePage(self.browser)
        self.findpage = FindPage(self.browser)
        self.detailpage = DetailPage(self.browser)
        self.addnewvisitpage = AddNewVisitPage(self.browser)
        
        self.detailpage = DetailPage(self.browser)
        self.homepage.goto_search()
        
        self.findpage.goto_detail_page()
        
        self.detailpage.goto_edit()
        self.editownerpage.edit_info(R1)
        
    def test_path5(self):
        self.homepage = HomePage(self.browser)
        self.findpage = FindPage(self.browser)
        self.detailpage = DetailPage(self.browser)
        self.editownerpage = EditOwnerPage(self.browser)
        
        self.detailpage = DetailPage(self.browser)
        self.homepage.goto_register()
        self.registerpage.regist_owner(R2)
        
    def test_path6(self):
        self.homepage = HomePage(self.browser)
        self.registerpage = RegisterPage(self.browser)
        
        self.homepage.goto_register()
        self.registerpage.regist_owner(R1)
        
        self.findpage.goto_detail_page()
        
    def test_path7(self):
        self.homepage = HomePage(self.browser)
        self.registerpage = RegisterPage(self.browser)
        self.findpage = FindPage(self.browser)
        
        self.detailpage = DetailPage(self.browser)
        self.homepage.goto_Veter()
        
    def test_path8(self):
        self.homepage = HomePage(self.browser)
        
        self.veterpage = VeterPage(self.browser)



if __name__ == '__main__':
    unittest.main()