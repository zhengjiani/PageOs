# -*- coding: UTF-8 -*-
import random
import time
from bok_choy.page_object import PageObject
from util.UpLoad import upload
class BasePage(PageObject):
    @property
    def url(self):
        return "zhengjiani.cn:8080/#/{0}".format(self.name)

class SearchPage(PageObject):
    """
    查找功能页面对象
    """
    url = None
    
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').is_present
    def search(self):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').click()
    def enter_search_items(self,*args):
        if len(args)==1:
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/input').fill(args[0])
            self.search()
        elif len(args)==2:
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/input').fill(args[0])
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/input').fill(args[1])
            self.search()
        else:
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/input').fill(args[0])
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/input').fill(args[1])
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div[3]/div[2]/input').fill(args[2])
            self.search()
class SelectUserPage(PageObject):
    '''
    选择
    '''
    url = None
    def is_browser_on_page(self):
        label = self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/label').text
        return label == ['用户名']
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
class AddPage(PageObject):
    """
    添加
    """
    url = None
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[2]').is_present
    def add_btn(self):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[2]').click()
    def confirm_btn(self):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div/button[2]').click()
    def cancel(self):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[3]/div/button[1]')
    def add_user(self, name, phone, passwd, gender_key, level_key, state_key, birthday):
        self.add_btn()
        self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/li').click()
        self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/li/ul/a[1]').click()
        self.wait_for_element_visibility('#app > div > div.main-container > section > div > div.filter-container > button:nth-child(4)','visible',timeout=10)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[2]').click()
        self.wait_for_element_visibility('#app > div > div.main-container > section > div > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium','visible',timeout=10)
        params=[[name,1],[phone,2],[passwd,3]]
        for param in params:
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[{}]/div/div/input'.format(param[1])).fill(param[0])
            time.sleep(2)
        SelectUserPage(self.browser).select_gender(gender_key)
        SelectUserPage.select_birthday(birthday)
        SelectUserPage.select_user_level(level_key)
        SelectUserPage.select_state(state_key)
        time.sleep(5)
        self.confirm_btn()
    def add_brand(self,bname,bcontent,bprice,imgpath):
        self.add_btn()
        params = [[bname, 1], [bcontent, 2], [bprice, 4]]
        for param in params:
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[{}]/div/div/input'.format(param[1])).fill(param[0])
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div/div').click()
        upload(imgpath)
        self.confirm_btn()
    def add_keyword(self,keyword,link):
        self.add_btn()
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div/input').fill(keyword)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div/input').fill(link)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div/div/span/span/i').click()
        self.q(xpath='/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[4]/div/div/div/span/span/i').click()
        self.q(xpath='/html/body/div[6]/div[1]/div[1]/ul/li[1]').click()
        #确定
        self.confirm_btn()
    def add_product(self,number,pname,zprice,cprice,pimgpath,drawpath):
        self.wait_for_element_visibility('#app > div > div.main-container > section > div > div:nth-child(1) > div > form > div:nth-child(11) > div > button','desc',timeout=10)
        params = [[number, 1], [pname, 2], [zprice, 3],[cprice,4]]
        for param in params:
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[{}]/div/div/input'.format(param[1])).fill(param[0])
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[5]/div/div/label[1]').click()
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[6]/div/div/label[1]').click()
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[7]/div/div/label[1]').click()
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[8]/div/div/div').click()
        upload(pimgpath)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[9]/div/div/div').click()
        upload(drawpath)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[5]/button[2]').click()
    def add_ad(self,ad_title,ad_content,ad_img,ad_link):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div/input').fill(ad_title)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div/input').fill(ad_content)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div/div').click()
        upload(ad_img)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[5]/div/div/input').fill(ad_link)
        #确认
        self.confirm_btn()
    def add_topic(self, title, sub_title, topic_img, low_price, read_nums):
        self.q(xoath='//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[2]/form/div[1]/div/div[1]/input').fill(title)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[2]/form/div[2]/div/div[1]/input').fill(sub_title)
        upload(topic_img)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[2]/form/div[5]/div/div/input').fill(low_price)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[2]/form/div[6]/div/div/input').fill(read_nums)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[5]/div/div[3]/div/button[2]').click()
    def add_admin(self, aname, apasswd, emojpath):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div/input').fill(aname)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div/input').fill(apasswd)
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div/div').click()
        upload(emojpath)
        self.confirm_btn()
    def add_object(self):
        pass
    def add_rule(self,good_id,discount,group_nums,out_date):
        self.add_btn()
        params = [[good_id, 1], [discount, 2], [group_nums, 3],[out_date,4]]
        for param in params:
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/form/div[{}]/div/div/input'.format(
                param[1])).fill(param[0])
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[3]/div/button[2]').click()

class SearchResultPage(PageObject):
    """
    添加结果
    """
    url=None
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]').is_present()
    def is_intable(self, name):
        self.wait_for_element_visibility(
            '#app > div > div.main-container > section > div > div.el-table.el-table--fit.el-table--border.el-table--enable-row-hover.el-table--enable-row-transition.el-table--small > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1) > td.el-table_1_column_1.is-center',
            'present'
            'present', timeout=10)
        n = len(self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr'))
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
        for i in range(1, n + 1):
            tr = self.q(
                xpath='//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[{}]'.format(i)).text
            print(tr)
    def search_user_result(self,user_name):
        self.is_intable(user_name)
class GetDataPage(PageObject):
    """
    获取数据页面对象
    """
    url = None
    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[2]').is_present
    def get_table_data(self):
        arr = []
        #按行查询表格数据
        table_tr_list = self.q(xpath= '//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr').text
        for tr in table_tr_list:
            arr1 = tr.split(" ")
            arr.append(arr1[0])
        return arr
class LoginPage(BasePage):
    """
    登录
    """
    name = 'login?redirect=%2Fdashboard'

    def is_browser_on_page(self):
        return self.q(xpath='//*[@id="app"]/div/form/button').is_present

    def login(self, username, password):
        self.q(xpath='//*[@id="app"]/div/form/div[2]/div/div/input').fill(username)
        self.q(xpath='//*[@id="app"]/div/form/div[3]/div/div/input').fill(password)
        self.q(xpath='//*[@id="app"]/div/form/button').click()
        HomePage(self.browser).wait_for_page()

class HomePage(BasePage):
    """
    主页
    """
    name = 'dashboard'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span/span[1]/span').text
        return title == ['首页']
    #链接测试
    def goto_user(self):
        dict_user = {
            1: UserPage(self.browser),
            2: AddressPage(self.browser),
            3: CollectPage(self.browser),
            4: FootprintPage(self.browser),
            5: HistoryPage(self.browser),
            6: FeedbackPage(self.browser)
        }
        self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/li').click()
        for k in sorted(dict_user.keys()):
            self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/li/ul/a[{}]'.format(k)).click()
            dict_user.get(k).wait_for_page(timeout=2)
    def goto_region(self):
        dict_mall = {
            1: RegionPage(self.browser),
            2: BrandPage(self.browser),
            3: CategoryPage(self.browser),
            4: OrderPage(self.browser),
            5: IssuePage(self.browser),
            6: KeywordPage(self.browser)
        }
        self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[3]/li').click()
        for k in sorted(dict_mall.keys()):
            self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[3]/li/ul/a[{}]'.format(k)).click()
            dict_mall.get(k).wait_for_page(timeout=2)
    def goto_good(self):
        dict_good = {
            1: GoodPage(self.browser),
            2: CreatePage(self.browser),
            3: CommentPage(self.browser),
        }
        self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[4]/li').click()
        for k in sorted(dict_good.keys()):
            self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[4]/li/ul/a[{}]'.format(k)).click()
            dict_good.get(k).wait_for_page(timeout=2)
    def goto_promotion(self):
        dict_promotion = {
            1: PromotionPage(self.browser),
            2: TopicPage(self.browser),
            3: Groupon_rulePage(self.browser),
            4: Groupon_activityPage(self.browser)
        }
        self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[5]/li').click()
        for k in sorted(dict_promotion.keys()):
            self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[5]/li/ul/a[{}]'.format(k)).click()
            dict_promotion.get(k).wait_for_page(timeout=2)
    def goto_sys(self):
        dict_sys = {
            1: SysPage(self.browser),
            2: OsPage(self.browser)
        }
        self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[6]/li').click()
        for k in sorted(dict_sys.keys()):
            self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[6]/li/ul/a[{}]'.format(k)).click()
            dict_sys.get(k).wait_for_page(timeout=2)
    def goto_stat(self):
        dict_stat = {
            1: StatPage(self.browser)
        }
        self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[7]/li').click()
        for k in sorted(dict_stat.keys()):
            self.q(xpath='//*[@id="app"]/div/div[1]/div[1]/div/ul/div[7]/li/ul/a[{}]'.format(k)).click()
            dict_stat.get(k).wait_for_page(timeout=2)
    def logout(self):
        self.q(xpath='//*[@id="dropdown-menu-8991"]/li[4]').click()
        LoginPage(self.browser).wait_for_page()

class ModifyPasswordPage(BasePage):
    """
    修改密码页
    """
    name='ModifyPasswordPage'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[2]/span[1]/span').text
        return title == ['修改密码']
    def modify_password(self,ori_passwd,new_password):
        params = [[ori_passwd, 1], [new_password, 2], [new_password, 3]]
        for param in params:
            self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[{}]/div/div/input'.format(param[1])).fill(param[0])
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div/button[2]').click()
        ModifyPasswordPage(self.browser).wait_for_page()

class UserPage(BasePage):
    """
    用户管理/会话管理
    """
    name = 'user/user'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['会员管理']
    def search_user(self,user_name,user_num):
        SearchPage(self.browser).enter_search_items(user_name,user_num)
        UserPage(self.browser).wait_for_page()
    def add_user(self, name, phone, passwd, gender_key, level_key, state_key, birthday):
        AddPage(self.browser).add_user( name, phone, passwd, gender_key, level_key, state_key, birthday)
        UserPage(self.browser).wait_for_page()
    def get_user_data(self):
        arr = GetDataPage(self.browser).get_table_data()
        s_arr = random.sample(arr, 1)[0].split("\n")[1:3]
        return s_arr

class AddressPage(BasePage):
    """
    用户管理/收货地址页
    """
    name='user/address'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['收货地址']
    def search_address(self,user_name,recv_name):
        SearchPage(self.browser).enter_search_items(user_name,recv_name)
        AddressPage(self.browser).wait_for_page()

class CollectPage(BasePage):
    """
    用户管理/会员收藏页
    """
    name='user/collect'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['会员收藏']
    def search_collect(self,user_id,good_id):
        SearchPage(self.browser).enter_search_items(user_id,good_id)
        CollectPage(self.browser).wait_for_page()

class FootprintPage(BasePage):
    """
    用户管理/会员足迹页
    """
    name='user/footprint'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['会员足迹']
    def search_footprint(self,user_id,good_id):
        SearchPage(self.browser).enter_search_items(user_id,good_id)
        FootprintPage(self.browser).wait_for_page()

class HistoryPage(BasePage):
    """
    用户管理/搜索历史页
    """
    name='user/history'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['搜索历史']
    def search_history(self,user_id,key_word):
        SearchPage(self.browser).enter_search_items(user_id,key_word)
        HistoryPage(self.browser).wait_for_page()

class FeedbackPage(BasePage):
    """
    用户管理/意见反馈页
    """
    name='user/feedback'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['意见反馈']
    def search_feedback(self,user_name,feedback_id):
        SearchPage(self.browser).enter_search_items(user_name,feedback_id)
        FeedbackPage(self.browser).wait_for_page()
#Mall
class RegionPage(BasePage):
    """
    商场管理/行政区域页
    """
    name='mall/region'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['行政区域']
    def search_region(self,region_name,region_num):
        SearchPage(self.browser).enter_search_items(region_name,region_num)
        RegionPage(self.browser).wait_for_page()

class BrandPage(BasePage):
    """
    商场管理/品牌制造商
    """
    name = 'mall/brand'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['品牌制造商']
    def search_brand(self,brand_id,brand_name):
        SearchPage(self.browser).enter_search_items(brand_id,brand_name)
        BrandPage(self.browser).wait_for_page()
    def add_brand(self,bname,bcontent,bprice,imgpath):
        AddPage(self.browser).add_brand(bname,bcontent,bprice,imgpath)
        BrandPage(self.browser).wait_for_page()
class CategoryPage(BasePage):
    """
    商场管理/商场类目
    """
    name='mall/category'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['商品类目']
    def search_category(self,cate_id,cate_name):
        SearchPage(self.browser).enter_search_items(cate_id,cate_name)
        CategoryPage(self.browser).wait_for_page()

class OrderPage(BasePage):
    """
    商场管理/订单管理页
    """
    name = 'mall/order'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['订单管理']
    def search_order(self,user_id,user_num,orderstate):
        SearchPage(self.browser).enter_search_items(user_id,user_num,orderstate)
        OrderPage(self.browser).wait_for_page()

class IssuePage(BasePage):
    """
    商场管理/通用问题页
    """
    name = 'mall/issue'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['通用问题']
    def search_issue(self,issue):
        SearchPage(self.browser).enter_search_items(issue)
        IssuePage(self.browser).wait_for_page()

class KeywordPage(BasePage):
    """
    商场管理/关键词页
    """
    name = 'mall/keyword'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['关键词']
    def search_keyword(self,keyword,link):
        SearchPage(self.browser).enter_search_items(keyword,link)
        KeywordPage(self.browser).wait_for_page()
    def add_keyword(self,keyword,link):
        AddPage(self.browser).add_keyword(keyword,link)
        KeywordPage(self.browser).wait_for_page()

#Goods
class GoodPage(BasePage):
    """
    商品管理/商品列表
    """
    name = 'goods/list'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['商品列表']
    def search_good(self,good_num,good_name):
        SearchPage(self.browser).enter_search_items(good_num,good_name)
        GoodPage(self.browser).wait_for_page()
    def add_good(self):
        self.q(xpath='//*[@id="app"]/div/div[2]/section/div/div[1]/button[2]').click()
        CreatePage(self.browser).wait_for_page()
class CreatePage(BasePage):
    """
    商品管理/商品上架
    """
    name = 'goods/create'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['商品上架']
    def add_good(self,number,pname,zprice,cprice,pimgpath,drawpath):
        AddPage(self.browser).add_product(number,pname,zprice,cprice,pimgpath,drawpath)
        GoodPage(self.browser).wait_for_page()
class CommentPage(BasePage):
    """
    商品管理/商品评论
    """
    name='goods/comment'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['商品评论']
    def search_comment(self,user_id,good_id):
        SearchPage(self.browser).enter_search_items(user_id,good_id)
        CommentPage(self.browser).wait_for_page()
#Promotion
class PromotionPage(BasePage):
    """
    推广管理/广告列表
    """
    name='promotion/ad'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['广告列表']
    def search_promotion(self,ad_title,ad_content):
        SearchPage(self.browser).enter_search_items(ad_title,ad_content)
        PromotionPage(self.browser).wait_for_page()
    def add_ad(self,ad_title,ad_content,ad_img,ad_link):
        AddPage(self.browser).add_ad(ad_title,ad_content,ad_img,ad_link)
        PromotionPage(self.browser).wait_for_page()
class TopicPage(BasePage):
    """
    推广管理/专题管理
    """
    name='promotion/topic'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['专题管理']
    def add_topic(self,title,sub_title,topic_img,topic_content,low_price,read_nums):
        AddPage.add_topic(title,sub_title,topic_img,topic_content,low_price,read_nums)
        TopicPage(self.browser).wait_for_page()
class Groupon_rulePage(BasePage):
    """
    推广管理/团购规则
    """
    name = 'promotion/groupon-rule'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['团购规则']
    def search_rule(self,good_num):
        SearchPage(self.browser).enter_search_items(good_num)
    def add_rule(self,good_id,discount,group_nums,out_date):
        AddPage(self.browser).add_rule(good_id,discount,group_nums,out_date)
class Groupon_activityPage(BasePage):
    """
    推广管理/团购活动
    """
    name='promotion/groupon-activity'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['团购活动']
    def search_activity(self,good_num):
        SearchPage(self.browser).enter_search_items(good_num)

#Sys
class SysPage(BasePage):
    """
    系统管理/管理员
    """
    name = 'sys/admin'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['管理员']
    def add_admin(self, aname, apasswd, emojpath):
        AddPage(self.browser).add_admin(self, aname, apasswd, emojpath)
class OsPage(BasePage):
    """
    系统管理/对象存储
    """
    name='sys/os'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['对象存储']
    def add_object(self):
        AddPage(self.browser).add_object()
class StatPage(BasePage):
    """
    统计
    """
    name='StatPage'
    def is_browser_on_page(self):
        title = self.q(xpath='//*[@id="app"]/div/div[2]/div[1]/div[2]/span/span[3]/span[1]/span').text
        return title == ['用户统计']

