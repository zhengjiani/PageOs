import lxml
import time
from lxml import etree
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://localhost:9527/#/login?redirect=%2Fuser%2Fuser')
driver.find_element_by_xpath("//*[@id='app']/div/form/div[2]/div/div/input").send_keys('')
driver.find_element_by_xpath("//*[@id='app']/div/form/div[3]/div/div/input").send_keys('')
driver.find_element_by_xpath("//*[@id='app']/div/form/button").click()
time.sleep(2)
cookie_list = driver.get_cookies()
for item in cookie_list: driver.add_cookie(
    {
        'domain': 'localhost',
        'httpOnly': False,
        'name': 'X-Litemall-Admin-Token',
        'path': '/',
        'secure': False,
        'value': '1fpzctbhesj4eqfg5e2k6gkg77m2u220'
    }
)
time.sleep(5)
def get_xpath(html):
    page=etree.HTML(html)
    result=page.xpath('//*')
    with open('D:\\code\\python\\bok-choy-master\\tests\\demo\\pathx','w') as f:
        for i in result:
            tree=lxml.etree.ElementTree(i)
            ll=tree.getpath(i)
            f.write(ll)
def get_leaf_xpath():
    result=[]
    with open('D:\\code\\python\\bok-choy-master\\tests\\demo\\pathx','r') as f:
        for line in f.readlines():
            result.append(line.strip('\n'))
    print(len(result))
    leaf_node_xpath_list=[]
    for i in range(len(result)-1):
        j=i+1
        one_xpath=result[i]
        two_xpath=result[j]
        if one_xpath in two_xpath:
            one_xpath=two_xpath
            two_xpath=result[j+1]
        else:
            leaf_node_xpath_list.append(one_xpath)
    return leaf_node_xpath_list
if __name__ == '__main__':
    driver.get('http://localhost:9527/#/user/user')
    html1=driver.page_source
    print(len(get_leaf_xpath()))
    driver.close()
