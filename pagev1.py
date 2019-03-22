# -*- coding: UTF-8 -*-
import time
from bok_choy.page_object import PageObject
from tests.demo.UpLoad import upload
class BasePage(PageObject):
    @property
    def url(self):
        return "http://localhost:9527/#/{}".format(self.name)
    def search(self,*args):
        if len(args)==1:
            time.sleep(5)
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/input').fill(args[0])
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').click()
        elif len(args)==2:
            time.sleep(5)
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/input').fill(args[0])
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/input').fill(args[1])
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').click()
        else:
            time.sleep(5)
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/input').fill(args[0])
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/input').fill(args[1])
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[3]/div[2]/input').fill(args[2])
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').click()
class LoginPage(PageObject):
    url= 'http://localhost:9527/#/login?redirect=%2Fdashboard'
    name = 'LoginPage'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/form/button').is_present
    def login(self,username,password):
        self.q(xpath='//*[@id="app"]/div/form/div[2]/div/div/input').fill(username)
        self.q(xpath='//*[@id="app"]/div/form/div[3]/div/div/input').fill(password)
        self.q(xpath='//*[@id="app"]/div/form/button').click()
class GotoPage(PageObject):
    '''
    跳转页
    '''
    url=None
    name='GotoPage'
    def jump(self,major,sub):
        major_titles={
            '用户管理': 1,
            '商场管理': 2,
            '商品管理': 3,
            '推广管理': 4,
            '系统管理': 5,
            '统计': 6
        }
        sub_titles={
            '用户管理': [['会员管理',1],['收货地址',2],['会员收藏',3],['会员足迹',4],['搜索历史',5]],
            '商场管理': [['行政区域',1],['品牌制造商',2],['商品类目',3],['订单管理',4],['通用问题',5],['关键词',6]],
            '商品管理': [['商品列表',1],['商品上架',2],['商品评论',3]],
            '推广管理': [['广告列表',1],['专题管理',2],['团购规则',3],['团购活动',4]],
            '系统管理': [['管理员',1],['对象存储',2]],
            '统计': [['用户统计',1],['订单统计',2],['商品统计',3]]
        }
        for k,v in sub_titles.items():
            if major==k and sub==v[0]:
                self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[{0}]/li/ul/a[{1}]'.format(major_titles.get(k),v[1])).click()
class AddPage(PageObject):
    def select_gender(self, gender_key):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[4]/div/div').click()
        gender_keys = {
            '未知': 1,
            '男': 2,
            '女': 3
        }
        i = gender_keys.get(gender_key)
        # 随机进行下拉彩单点击
        self.q(xpath='/html/body/div[3]/div[1]/div[1]/ul/li[{}]'.format(i)).click()

    def select_birthday(self, birthday):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[5]/div/div/input').fill(
            birthday)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[5]/label').click()

    def select_user_level(self, level_key):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[6]/div/div/div').click()
        level_keys = {
            '普通用户': 1,
            'VIP用户': 2,
            '高级VIP用户': 3
        }
        i = level_keys.get(level_key)
        self.q(xpath='/html/body/div[6]/div[1]/div[1]/ul/li[{}]'.format(i)).click()
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[6]/label').click()

    def select_state(self, state_key):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[7]/div/div/div').click()
        state_keys = {
            '可用': 1,
            '禁用': 2,
            '注销': 3
        }
        i = state_keys.get(state_key)
        self.q(xpath='/html/body/div[5]/div[1]/div[1]/ul/li[{}]'.format(i)).click()
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[7]/label').click()

    def add_user(self, name, phone, passwd, gender_key, level_key, state_key, birthday):
        self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[3]/div[1]').click()
        self.wait_for_element_visibility(
            '#app > div > div.main-container > section > div > div.filter-container > button:nth-child(4)',
            'kejian', timeout=5)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[2]').click()
        self.wait_for_element_visibility(
            '#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > input',
            'visible', timeout=5)
        params=[[name,1],[phone,2],[passwd,3]]
        for param in params:
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[{}]/div/div/input'.format(param[1])).fill(param[0])
            time.sleep(2)
        self.select_gender(gender_key)
        self.select_birthday(birthday)
        self.select_user_level(level_key)
        self.select_state(state_key)
        time.sleep(5)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div/button[2]').click()
        self.wait_for_element_visibility(
            '#app > div > div.main-container > section > div > div.filter-container > button:nth-child(3)',
            'visible', timeout=10)
    def add_brand(self,bname,bcontent,bprice,imgpath):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[2]').click()
        params = [[bname, 1], [bcontent, 2], [bprice, 4]]
        for param in params:
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[{}]/div/div/input'.format(param[1])).fill(param[0])
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div/div').click()
        upload(imgpath)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div/button[2]').click()
    def add_product(self,number,pname,zprice,cprice,pimgpath,drawpath):
        params = [[number, 1], [pname, 2], [zprice, 3],[cprice,4]]
        for param in params:
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[{}]/div/div/input'.format(param[1])).fill(param[0])
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[5]/div/div/label[1]/span[1]/input').click()
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[6]/div/div/label[1]/span[1]/input').click()
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[7]/div/div/label[1]/span[1]/input').click()
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[8]/div/div/div').click()
        upload(pimgpath)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[9]/div/div/div').click()
        upload(drawpath)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[5]/button[2]').click()

    def add_admin(self, aname, apasswd, emojpath):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[2]').click()
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div/input').fill(aname)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div/input').fill(apasswd)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div/div').click()
        upload(emojpath)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div/button[2]').click()
class ModifyPasswordPage(PageObject):
    url='http://localhost:9527/#/profile/password'
    name='ModifyPasswordPage'
    def modify_password(self,ori_passwd,new_password):
        params = [[ori_passwd, 1], [new_password, 2], [new_password, 3]]
        for param in params:
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[{}]/div/div/input'.format(param[1])).fill(param[0])
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div/button[2]').click()
class ResultPage(PageObject):
    url=None
    name='ResultPage'
    def is_intable(self, name):
        self.wait_for_element_visibility(
            '#app > div > div.main-container > section > div > div.el-table.el-table--fit.el-table--border.el-table--enable-row-hover.el-table--enable-row-transition.el-table--small > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1) > td.el-table_1_column_1.is-center',
            'present'
            'present', timeout=10)
        n = len(self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr'))
        print(n)
        for i in range(1, n + 1):
            tr = self.q(
                xpath='//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[{}]'.format(i)).text
            str = "\n".join(tr)
            print(str)
            if name in str:
                return True
            else:
                raise ValueError('Not in this table')
    def show_result_detail(self):
        self.wait_for_element_visibility(
            '#app > div > div.main-container > section > div > div.el-table.el-table--fit.el-table--border.el-table--enable-row-hover.el-table--enable-row-transition.el-table--small > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1) > td.el-table_1_column_1.is-center',
            'present', timeout=10)
        n = len(self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr'))
        print(n)
        for i in range(1, n + 1):
            tr = self.q(
                xpath='//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[{}]'.format(i)).text
            print(tr)
class UserPage(BasePage,AddPage):
    name='user/user'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/span[2]').is_present
class MallPage(BasePage):
    name='mall/region'
class AddressPage(BasePage):
    name='user/address'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').is_present
class CollectPage(BasePage):
    name='user/collect'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').is_present
class FootprintPage(BasePage):
    name='user/footprint'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').is_present
class HistoryPage(BasePage):
    name='user/history'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').is_present
class FeedbackPage(BasePage):
    name='user/feedback'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').is_present
class BrandPage(BasePage):
    name = 'mall/brand'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/span[3]').is_present
class CategoryPage(BasePage):
    name='mall/category'
class OrderPage(BasePage):
    name = 'mall/order'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/span[3]').is_present
class IssuePage(BasePage):
    name = 'mall/issue'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/span[4]').is_present
class KeywordPage(BasePage):
    name = 'mall/keyword'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/span[7]').is_present
class GoodPage(BasePage):
    name = 'goods/list'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/span[5]').is_present
class CreatePage(PageObject):
    url='http://localhost:9527/#/goods/create'
    name = 'CreatePage'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/span[9]').is_present
class CommentPage(BasePage):
    name='goods/comment'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').is_present
class PromotionPage(BasePage):
    name='promotion/ad'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').is_present
class TopicPage(BasePage):
    name='promotion/topic'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').is_present
class Groupon_rulePage(BasePage):
    name = 'promotion/groupon-rule'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').is_present
class Groupon_activityPage(BasePage):
    name='promotion/groupon-activity'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').is_present
class SysPage(BasePage):
    name = 'sys/admin'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/span[15]').is_present
class OsPage(BasePage):
    name='sys/os'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').is_present
class StatPage(PageObject):
    name='StatPage'
    url='stat/user'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div').is_present
class LogoutPage(PageObject):
    url = None
    name = 'LogoutPage'
    def logout(self):
        self.q(xpath='//*[@id="dropdown-menu-8991"]/li[4]').click()
        LoginPage(self.browser).wait_for_page()
