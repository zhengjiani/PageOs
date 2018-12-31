# -*- coding: UTF-8 -*-
import time
from bok_choy.page_object import PageObject
from tests.demo.UpLoad import upload
class LoginPage(PageObject):
    '''
    管理员登录页
    '''
    url= 'http://localhost:9527/#/login?redirect=%2Fdashboard'
    name = 'LoginPage'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/form/button').is_present
    def login(self,username,password):
        self.q(xpath='//*[@id="app"]/div/form/div[2]/div/div/input').fill(username)
        self.q(xpath='//*[@id="app"]/div/form/div[3]/div/div/input').fill(password)
        self.q(xpath='//*[@id="app"]/div/form/button').click()
        HomePage(self.browser).wait_for_page()
class HomePage(PageObject):
    '''
    主页：用于跳转
    '''
    url='http://localhost:9527/#/dashboard'
    name = 'HomePage'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/div[1]').is_present
    # 用户管理
    def jump_user_page(self):
        self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/li/ul/a[1]/li').click()
        # print('success')
        UserPage(self.browser).wait_for_page()
    # 商场管理
    def jump_mall_page(self):
        self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[3]/li/ul/a[1]/li').click()
        MallPage(self.browser).wait_for_page()
    # 商品管理
    def jump_goods_page(self):
        self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[4]/li/ul/a[1]/li').click()
        GoodPage(self.browser).wait_for_page()
    # 推广管理
    def jump_promotion_page(self):
        self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[5]/li/ul/a[1]/li').click()
        PromotionPage(self.browser).wait_for_page()
    # 系统管理
    def jump_sys_page(self):
        self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[6]/li/ul/a[1]/li').click()
        SysPage(self.browser).wait_for_page()
    # 统计
    def jump_stat_page(self):
        self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[7]/li/ul/a[1]/li').click()
        StatPage(self.browser).wait_for_page()
    def jump(self,option):
        options={
            '用户管理': self.jump_user_page,
            '商场管理': self.jump_mall_page,
            '商品管理': self.jump_goods_page,
            '推广管理': self.jump_promotion_page,
            '系统管理': self.jump_sys_page,
            '统计': self.jump_stat_page
        }
        method=options.get(option)
        if method:
            method()
class UserPage(PageObject):
    '''
    用户管理页测试
    '''
    url='http://localhost:9527/#/user/user'
    name='UserPage'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/span[2]').is_present
    def search_user(self,name,phone):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/input').fill(name)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/input').fill(phone)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').click()
        ResultUserPage(self.browser).wait_for_page()
    #input元素做的伪下拉框，无法使用select定位
    def select_gender(self,gender_key):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[4]/div/div').click()
        gender_keys={
            '未知':1,
            '男':2,
            '女':3
        }
        i=gender_keys.get(gender_key)
        #随机进行下拉彩单点击
        self.q(xpath='/html/body/div[3]/div[1]/div[1]/ul/li[{}]'.format(i)).click()
    def select_birthday(self,birthday):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[5]/div/div/input').fill(birthday)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[5]/label').click()
    def select_user_level(self,level_key):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[6]/div/div/div').click()
        level_keys={
            '普通用户':1,
            'VIP用户':2,
            '高级VIP用户':3
        }
        i=level_keys.get(level_key)
        self.q(xpath='/html/body/div[6]/div[1]/div[1]/ul/li[{}]'.format(i)).click()
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[6]/label').click()
    def select_state(self,state_key):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[7]/div/div/div').click()
        state_keys={
            '可用':1,
            '禁用':2,
            '注销':3
        }

        i=state_keys.get(state_key)
        self.q(xpath='/html/body/div[5]/div[1]/div[1]/ul/li[{}]'.format(i)).click()
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[7]/label').click()
    def add_user(self,name,phone,passwd,gender_key,level_key,state_key,birthday):
        self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[3]/div[1]').click()
        self.wait_for_element_visibility('#app > div > div.main-container > section > div > div.filter-container > button:nth-child(4)','kejian',timeout=5)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[2]').click()
        self.wait_for_element_visibility('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__body > form > div:nth-child(1) > div > div > input','visible',timeout=5)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div/input').fill(name)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div/input').fill(phone)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div/input').fill(passwd)
        self.select_gender(gender_key)
        self.select_birthday(birthday)
        self.select_user_level(level_key)
        self.select_state(state_key)
        time.sleep(5)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div/button[2]').click()
        self.wait_for_element_visibility('#app > div > div.main-container > section > div > div.filter-container > button:nth-child(3)','visible',timeout=10)
    def jump_others(self,option):
        options={
            '收货地址':2,
            '会员收藏':3,
            '会员足迹':4,
            '搜索历史':5
        }
        i=options.get(option)
        self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/li/ul/a[{}]'.format(i)).click()
        if i==2:
            AddressPage(self.browser).wait_for_page()
        elif i==3:
            CollectPage(self.browser).wait_for_page()
        elif i==4:
            FootprintPage(self.browser).wait_for_page()
        elif i==5:
            HistoryPage(self.browser).wait_for_page()
        else:
            raise ValueError('Not in right page')
class AddressPage(PageObject):
    url='http://localhost:9527/#/user/address'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').is_present
    print('oh yeah')
class CollectPage(PageObject):
    pass
class FootprintPage(PageObject):
    pass
class HistoryPage(PageObject):
    pass

class ResultUserPage(PageObject):
    '''
    用户查询结果页
    '''
    url='http://localhost:9527/#/user/user'
    name='ResultUserPage'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/input').is_present
    def is_intable(self,name):
        self.wait_for_element_visibility(
            '#app > div > div.main-container > section > div > div.el-table.el-table--fit.el-table--border.el-table--enable-row-hover.el-table--enable-row-transition.el-table--small > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1) > td.el-table_1_column_1.is-center','present'
            'present', timeout=10)
        n = len(self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr'))
        print(n)
        for i in range(1, n + 1):
            tr = self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[{}]'.format(i)).text
            str="\n".join(tr)
            print(str)
            if name in str:
                return True
            else:
                raise ValueError('Not in this table')
    @property
    def show_result_detail(self):
        '''
        展示所有的用户记录
        :return:
        '''
        self.wait_for_element_visibility('#app > div > div.main-container > section > div > div.el-table.el-table--fit.el-table--border.el-table--enable-row-hover.el-table--enable-row-transition.el-table--small > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1) > td.el-table_1_column_1.is-center','present',timeout=10)
        n=len(self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr'))
        print(n)
        for i in range(1,n+1):
            tr=self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[{}]'.format(i)).text
            print(tr)
class MallPage(PageObject):
    '''
    行政区域页测试：商场管理
    '''
    url='http://localhost:9527/#/mall/region'
    name = 'MallPage'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/span[2]').is_present
    def search(self,name,number):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/input').fill(name)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/input').fill(number)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').click()
    def download(self):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[2]').click()
    def check_total(self):
        #返回页底共多少条结果
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[3]/div/span[1]').text
class BrandPage(PageObject):
    '''
    品牌制造商页测试
    '''
    url='http://localhost:9527/#/mall/brand'
    name = 'BrandPage'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/span[3]').is_present
    def search(self,name,number):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/input').fill(name)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/input').fill(number)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').click()
    def add_brand(self):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[2]').click()
    def upgrate_brand(self,bname,bcontent,bprice,imgpath):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div/input').fill(bname)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div/input').fill(bcontent)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div/div').click()
        upload(imgpath)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[4]/div/div/input').fill(bprice)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div/button[2]').click()
        #return ResultaddPage(self.browser)
class OrderPage(PageObject):
    '''
    订单页测试
    '''
    url='http://localhost:9527/#/mall/order'
    name = 'OrderPage'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/span[3]').is_present
class IssuePage(PageObject):
    '''
    问题页测试
    '''
    url='http://localhost:9527/#/mall/issue'
    name = 'IssuePage'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/span[4]').is_present
class KeywordPage(PageObject):
    '''
    关键词页测试
    '''
    url='http://localhost:9527/#/mall/keyword'
    name = 'KeywordPage'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/span[7]').is_present
class CreatePage(PageObject):
    '''商品上架页测试'''
    url='http://localhost:9527/#/goods/create'
    name = 'CreatePage'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/span[9]').is_present
    def add_product(self,number,pname,zprice,cprice,pimgpath,drawpath):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div/div/input').fill(number)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div/div/input').fill(pname)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[3]/div/div/input').fill(zprice)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[4]/div/div/input').fill(cprice)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[5]/div/div/label[1]/span[1]/input').click()
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[6]/div/div/label[1]/span[1]/input').click()
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[7]/div/div/label[1]/span[1]/input').click()
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[8]/div/div/div').click()
        upload(pimgpath)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[9]/div/div/div').click()
        upload(drawpath)
        #上架
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[5]/button[2]').click()
        return ProductPage(self.browser)
class ProductPage(PageObject):
    '''
    商品列表详情页测试
    '''
    url = 'http://localhost:9527/#/goods/list'
    name = 'ProductPage'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/span[5]').is_present
class AdminPage(PageObject):
    '''
    用户管理页测试
    '''
    url='http://localhost:9527/#/sys/admin'
    name = 'AdminPage'
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/span[15]').is_present
    def add_admin(self):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[2]').click()
    def upgrate_admin(self,aname,apasswd,emojpath):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div/input').fill(aname)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div/input').fill(apasswd)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div/div').click()
        upload(emojpath)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div/button[2]').click()
class GoodPage(PageObject):
    pass
class PromotionPage(PageObject):
    pass
class SysPage(PageObject):
    pass
class StatPage(PageObject):
    pass
class LogoutPage(PageObject):
    '''登出页测试'''
    url = None
    name = 'LogoutPage'
    def logout(self):
        self.q(xpath='//*[@id="dropdown-menu-8991"]/li[4]').click()
        LoginPage(self.browser).wait_for_page()
