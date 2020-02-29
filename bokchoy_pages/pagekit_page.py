# -*- encoding: utf-8 -*-
"""
@File    : pagekit_page.py
@Time    : 2020/2/15 7:47 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
import os
from bok_choy.page_object import PageObject, unguarded
class BasePage(PageObject):
    SERVER_PORT = os.environ.get("SERVER_PORT", 3000)
    @property
    def url(self):
        return "http://localhost:{0}/#!/{1}".format(self.SERVER_PORT, self.name)
class InputUserPage(PageObject):
    url = None
    @unguarded
    def input_info(self,user_type,user_display,user_total,users_number):
        pass
    @unguarded
    def add_info(self, username,name,email,password,status):
        pass
    @unguarded
    def edit_info(self, username, name, email, password, status):
        pass
class InputLocPage(PageObject):
    url = None
    @unguarded
    def input_info(self, location,unit):
        pass
class InputFeedPage(PageObject):
    url = None
    @unguarded
    def input_info(self, feed_title,feed_url,feed_num,post_content):
        pass
class DeletePage(PageObject):
    @unguarded
    def delete(self,id):
        pass
# 导航对象
class DashboardPage(BasePage):
    def add_user(self,user_type,user_display,user_total,users_number):
        """
        :param user_type,user_display,user_total,users_number
        :return: DashboardPage
        """
        InputUserPage.input_info(user_type,user_display,user_total,users_number)
        return DashboardPage(self.browser).wait_for_page()
    def edit_user(self,user_id,user_type,user_display,user_total,users_number):
        """
        :param user_id,user_type,user_display,user_total,users_number
        :return: DashboardPage
        """
        user_id = 1
        InputUserPage.input_info(user_type, user_display, user_total, users_number)
        return DashboardPage(self.browser).wait_for_page()
    def goto_edit_user(self,user_id):
        """
        :param user_id:
        :return:AddEditUserPage
        """
        self.q(xpath=".//a[@href]").click()
        return AddEditUserPage(self.browser).wait_for_page()
    def add_location(self,location,unit):
        """
        :param location,unit
        :return: DashboardPage
        """
        InputLocPage.input_info(location,unit)
        return DashboardPage(self.browser).wait_for_page()
    def edit_location(self,user_id,location,unit):
        """
        :param user_id,location,unit
        :return: DashboardPage
        """
        InputLocPage.input_info(location,unit)
        return DashboardPage(self.browser).wait_for_page()
    def add_feed(self,feed_title,feed_url,feed_num,post_content):
        """
        :param feed_title,feed_url,feed_num,post_content
        :return: DashboardPage
        """
        InputFeedPage.input_info(feed_title,feed_url,feed_num,post_content)
        return DashboardPage(self.browser).wait_for_page()
    def edit_feed(self,feed_id,feed_title,feed_url,feed_num,post_content):
        """
        :param feed_title,feed_url,feed_num,post_content
        :return: DashboardPage
        """
        InputFeedPage.input_info(feed_id,feed_title,feed_url,feed_num,post_content)
        return DashboardPage(self.browser).wait_for_page()
    def delete_user_feed(self,user_id):
        """
        :param user_id:
        :return:DeleteItemPage
        """
        DeletePage.delete(user_id)
        return DeleteItemPage(self.browser).wait_for_page()
    def delete_location(self,loc_id):
        """
        :param loc_id:
        :return:DeleteItemPage
        """
        DeletePage.delete(loc_id)
        return DashboardPage(self.browser).wait_for_page()
    def goto_site(self):
        """
        :return: PagesPage
        """
        return PagesPage(self.browser).wait_for_page()
    def goto_users(self):
        """
        :return: UserListPage
        """
        return UserListPage(self.browser).wait_for_page()

class LoginPage(BasePage):
    def sign_in(self,username,password):
        """
        :param username,password
        :return: DashboardPage
        """
        self.q(xpath="//input[@name=\"credentials[username]\"]").fill(username)
        self.q(xpath="//input[@name=\"credentials[password]\"]").fill(password)
        self.q(xpath="(//button[1])[1]").click()
        return DashboardPage(self.browser).wait_for_page()

class AddEditUserPage(BasePage):
    def add_user(self,username,name,email,password,status):
        """
        :param username,name,email,password,status
        :return:AddEditUserPage
        """
        InputUserPage.add_info(username,name,email,password,status)
        return AddEditUserPage(self.browser).wait_for_page()
    def edit_user(self,username,name,email,password,status):
        """
        :param username,name,email,password,status
        :return:AddEditUserPage
        """
        InputUserPage.edit_info(username,name,email,password,status)
        return AddEditUserPage(self.browser).wait_for_page()
    def goto_dashboard(self):
        """
        :return: DashboardPage
        """
        return DashboardPage(self.browser).wait_for_page()
    def goto_users(self):
        """
        :return: UserListPage
        """
        return UserListPage(self.browser).wait_for_page()
    def goto_permission(self):
        """
        :return: PermissionsPage
        """
        return PermissionsPage(self.browser).wait_for_page()
    def goto_roles(self):
        """
        :return: RolesPage
        """
        return RolesPage(self.browser).wait_for_page()

class DeleteItemPage(BasePage):
    pass

class PagesPage(BasePage):
    def edit_menu(self,site_menu,new_name):
        """
        :param site_menu，new_name
        :return: AddEditItemPage
        """
        return AddEditItemPage(self.browser).wait_for_page()
    def add_menu(self,site_menu):
        """
        :param site_menu
        :return: AddEditItemPage
        """
        return AddEditItemPage(self.browser).wait_for_page()
    def publish_all_pages(self):
        """
        :return: PagesPage
        """
        return PagesPage(self.browser).wait_for_page()
    def unpublish_all_pages(self):
        """
        :return: PagesPage
        """
        return PagesPage(self.browser).wait_for_page()
    def delete_all_pages(self):
        """
        :return: PagesPage
        """
        return PagesPage(self.browser).wait_for_page()
    def delete_link(self):
        """
        :return: PagesPage
        """
        return PagesPage(self.browser).wait_for_page()
    def add_link(self):
        """
        :return: PagesPage
        """
        return AddEditLinkPage(self.browser).wait_for_page()

    def add_page(self):
        """
        :return: PagesPage
        """
        return AddEditPagePage(self.browser).wait_for_page()

class UserListPage(BasePage):
    def active_user(self,user_id):
        """
        :param user_id:
        :return:
        """
        return UserListPage(self.browser).wait_for_page()
    def block_user(self,user_id):
        """
        :param user_id:
        :return:
        """
        return UserListPage(self.browser).wait_for_page()


class SelectLinkPage(BasePage):
    pass


class UserSettingsPage(BasePage):
    def change_setting(self,regist_user_setting):
        """
        :param regist_user_setting:
        :return:SelectLinkPage
        """
        return SelectLinkPage(self.browser).wait_for_page()
    def save_setting(self):
        """
        :return: UserSettingsPage
        """
        return UserSettingsPage(self.browser).wait_for_page()

class PermissionsPage(BasePage):
    def edit_all_roles(self,user_roles):
        """
        :param user_roles:
        :return: PermissionsPage
        """
        return PermissionsPage(self.browser).wait_for_page()
    def goto_dashboard(self):
        """
        :return: DashboardPage
        """
        return DashboardPage(self.browser).wait_for_page()
    def goto_settings(self):
        """
        :return: DashboardPage
        """
        return UserSettingsPage(self.browser).wait_for_page()


class SelectImagePage(BasePage):
    pass


class AddEditItemPage(BasePage):
    def add_link(self,link_status,link_type,site_link,hide_menu):
        """
        :param link_status,link_type,site_link,hide_menu
        :return: AddEditLinkPage
        """
        return AddEditLinkPage(self.browser).wait_for_page()
    def add_link_Access(self,link_status,link_type,user_role,site_link,hide_menu):
        """
        :param link_status:,link_type,user_role,site_link,hide_menu
        :return: AddEditLinkPage
        """
        return AddEditLinkPage(self.browser).wait_for_page()
    def select_url(self):
        """
        :return: SelectLinkPage
        """
        return SelectLinkPage(self.browser).wait_for_page()
    def add_edit_meta(self,site_link,desc):
        """
        :param site_link,desc
        :return: SelectImagePage
        """
        return SelectImagePage(self.browser).wait_for_page()


class RolesPage(BasePage):
    def edit_all_roles(self,user_roles):
        """
        :param user_roles:
        :return: PermissionsPage
        """
        return RolesPage(self.browser).wait_for_page()
    def add_exist_role(self,user_role):
        """
        :param user_role
        :return: AddEditItemPage
        """
        return AddEditItemPage(self.browser).wait_for_page()
    def add_user_role(self,user_role):
        """
        :param user_role:
        :return: AddEditItemPage
        """
        return AddEditItemPage(self.browser).wait_for_page()
    def edit_user_role(self,user_role,new_user):
        """
        :param user_role:
        :return: AddEditItemPage
        """
        return AddEditItemPage(self.browser).wait_for_page()
    def delete_user_role(self,user_role):
        """
        :param user_role:
        :return: DeleteItemPage
        """
        return DeleteItemPage(self.browser).wait_for_page()

class AddEditLinkPage(BasePage):
    pass
class AddEditPagePage(BasePage):
    pass
