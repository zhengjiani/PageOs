# -*- encoding: utf-8 -*-
"""
@File    : pageKit_po_page.py
@Time    : 2020/4/15 6:08 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import os
from bok_choy.page_object import PageObject, unguarded
class BasePage(PageObject):
    pass
class DashboardPage(BasePage):
    def add_user(self,user_type,user_display,total_user,users_number):
        '''
        :param user_type:
        :param user_display:
        :param total_user:
        :param users_number:
        :return: DashboardPage
        '''
        pass
    def edit_user(self,id,user_type,user_display,total_user,users_number):
        '''
        :param id:
        :param user_type:
        :param user_display:
        :param total_user:
        :param users_number:
        :return: DashboardPage
        '''
        pass
    def go_edit_user(self,id):
        '''
        :param id:
        :return: AddEditUserPage
        '''
        pass
    def go_site(self):
        '''
        :return: PagesPage
        '''
    def go_users(self):
        '''
        :return: UserListPage
        '''
    def add_location(self,id,loc,unit):
        '''
        :param id:
        :param loc:
        :param unit:
        :return: DashboardPage
        '''
        pass
    def edit_location(self,id,loc,unit):
        '''
        :param id:
        :param loc:
        :param unit:
        :return: DashboardPage
        '''
    def add_feed(self,title,feed_url,posts,feed_post_content):
        '''
        :param title:
        :param feed_url:
        :param posts:
        :param feed_post_content:
        :return: DashboardPage
        '''
    def edit_feed(self,id,title,feed_url,posts,feed_post_content):
        '''
        :param id:
        :param title:
        :param feed_url:
        :param posts:
        :param feed_post_content:
        :return: DashboardPage
        '''
    def delete_user_feed(self,id):
        '''
        :param id:
        :return: DeleteItemPage
        '''
    def delete_loc(self,id):
        '''
        :param id:
        :return: DashboardPage
        '''
    def goto_content(self):
        '''
        :return: AddEditPagePage
        '''
class AddEditUserPage(BasePage):
    def add_user(self,username,name,email,password,status):
        '''
        :param username:
        :param name:
        :param email:
        :param password:
        :param status:
        :return: AddEditUserPage
        '''
    def edit_user(self,username,name,email,password):
        '''
        :param username:
        :param name:
        :param email:
        :param password:
        :return: AddEditUserPage
        '''
    def goto_user_list(self):
        '''
        :return: UserListPage
        '''
    def goto_roles(self):
        '''
        :return: RolesPage
        '''
    def goto_setting(self):
        '''
        :return: UserSettingPage
        '''
class DeleteItemPage(PageObject):
    pass
class PagesPage(BasePage):
    def publish_pages(self):
        '''
        :return: PagesPage
        '''
    def delete_pages(self):
        '''
        :return: PagesPage
        '''
    def unpublish_pages(self):
        '''
        :return: PagesPage
        '''
    def move_all_pages(self,site_menu):
        '''
        :return: PagesPage
        '''
    def delete_link(self,site_link):
        '''
        :param site_link:
        :return: PagesPage
        '''
    def edit_link(self,site_link):
        '''
        :param site_link:
        :return: AddEditLinkPage
        '''
class UserListPage(BasePage):
    def activate_user(self,id):
        '''
        :param id:
        :return: UserListPage
        '''
    def block_user(self,id):
        '''
        :param id:
        :return: UserListPage
        '''
    def delete_user(self,id):
        '''
        :param id:
        :return: DeleteItemPage
        '''
class SignInPage(BasePage):
    def sign_in(self,username,password):
        '''
        :param username:
        :param password:
        :return:DashboardPage
        '''
class AddEditLinkPage(BasePage):
    def add_link(self,link_status,link_type,hide_menu):
        '''
        :param link_status:
        :param link_type:
        :param hide_menu:
        :return: AddEditLinkPage
        '''
    def add_link_access(self,link_status,link_type,user_role,site_link,hide_menu):
        '''
        :param link_status:
        :param link_type:
        :param user_role:
        :param site_link:
        :param hide_menu:
        :return: AddEditLinkPage
        '''
    def select_url(self):
        '''
        :return: SelectLinkPage
        '''
    def add_edit_meta(self,site_link,meta_desc):
        '''
        :param site_link:
        :param meta_desc:
        :return: SelectImagePage
        '''
    def go_dashboard(self):
        '''
        :return: DashboardPage
        '''
class SelectLinkPage(PageObject):
    pass
class SelectImagePage(PageObject):
    pass
class AddEditLoginPage(BasePage):
    def add_details(self,login_title,link_status):
        '''
        :param login_title:
        :param link_status:
        :return: AddEditLoginPage
        '''
    def add_details_access(self,login_title,link_status,user_role):
        '''
        :param login_title:
        :param link_status:
        :param user_role:
        :return: AddEditLoginPage
        '''
    def select_login(self):
        '''
        :return: SelectLinkPage
        '''
    def select_logout(self):
        '''
        :return: SelectLinkPage
        '''
    def restrict_visible(self,site_page):
        '''
        :param site_page:
        :return: AddEditLoginPage
        '''
    def go_dashboard(self):
        '''
        :return: DashboardPage
        '''
class AddEditMenuPage(BasePage):
    def add_edit_menu(self,menu_title,site_menu,start_level,depth,menu_sub,link_status):
        '''
        :param menu_title:
        :param site_menu:
        :param start_level:
        :param depth:
        :param menu_sub:
        :param link_status:
        :return: AddEditMenuPage
        '''
    def add_edit_menu_access(self,menu_title,site_menu,start_level,depth,menu_sub,link_status,user_role):
        '''
        :param menu_title:
        :param site_menu:
        :param start_level:
        :param depth:
        :param menu_sub:
        :param link_status:
        :param user_role:
        :return: AddEditMenuPage
        '''
    def add_visible_link(self,site_link):
        '''
        :param site_link:
        :return: AddEditMenuPage
        '''
class AddEditTextPage(BasePage):
    def add_edit_text(self,text_title,html_snippet,link_status):
        '''
        :param text_title:
        :param html_snippet:
        :param link_status:
        :return: AddEditTextPage
        '''
    def add_edit_text_access(self,text_title,html_snippet,link_status,user_role):
        '''
        :param text_title:
        :param html_snippet:
        :param link_status:
        :param user_role:
        :return: AddEditTextPage
        '''
class PermissionsPage(BasePage):
    def operate_user_role(self,user_roles):
        '''
        :param user_roles:
        :return: PermissionsPage
        '''
class RolesPage(BasePage):
    def operate_user_roles(self,user_roles):
        '''
        :param user_roles:
        :return: RolesPage
        '''
    def delete_user_role(self,user_role):
        '''
        :param user_role:
        :return: DeleteItemPage
        '''
    def add_user_role(self,role_edit,exist_role):
        '''
        :param role_edit:
        :param exist_role:
        :return: AddEditItemPage
        '''
    def edit_user_role(self,role_edit,new_role):
        '''
        :param role_edit:
        :param new_role:
        :return: AddEditItemPage
        '''
class UserSettingPage(BasePage):
    def change_settings(self,regist_settings):
        '''
        :param regist_settings:
        :return: SelectLinkPage
        '''
    def save_settings(self):
        '''
        :return: UserSettingPage
        '''
class AddEditItemPage(PageObject):
    pass
class WidgetsPage(BasePage):
    def delete_widgets(self):
        '''
        :return: WidgetsPage
        '''
    def publish_widgets(self):
        '''
        :return: WidgetsPage
        '''
    def unpublish_widgets(self):
        '''
        :return: WidgetsPage
        '''
    def copy_widgets(self):
        '''
        :return: WidgetsPage
        '''
    def edit_menu(self,menu_title):
        '''
        :param menu_title:
        :return: AddEditMenuPage
        '''
    def edit_text(self,text_title):
        '''
        :param text_title:
        :return: AddEditTextPage
        '''
    def edit_login(self,login_title):
        '''
        :param login_title:
        :return: AddEditLoginPage
        '''
    def add_munu(self):
        '''
        :return: AddEditMenuPage
        '''
    def add_text(self):
        '''
        :return: AddEditTextPage
        '''
    def add_login(self):
        '''
        :return: AddEditLoginPage
        '''
    def go_Dashboard(self):
        '''
        :return: DashboardPage
        '''
class AddEditPagePage(BasePage):
    def add_edit(self,site_page,html_snippet,page_status,hode_menu):
        '''
        :param site_page:
        :param html_snippet:
        :param page_status:
        :param hode_menu:
        :return: AddEditPagePage
        '''
    def add_edit_access(self,site_page,html_snippet,page_status,user_role,hode_menu):
        '''
        :param site_page:
        :param html_snippet:
        :param page_status:
        :param user_role:
        :param hode_menu:
        :return: AddEditPagePage
        '''
    def add_edit_meta(self,site_page,meta_desc):
        '''
        :param site_page:
        :param meta_desc:
        :return: SelectItemPage
        '''

class SelectItemPage(PageObject):
    pass

