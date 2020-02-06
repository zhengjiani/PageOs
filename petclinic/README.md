# 使用原生Selenium测试petclinic网站
## package petclinic<br>
元素定位器——locators.py<br>
页面对象——page.py<br>
测试——test.py<br>

html-testrunner<br>
unittest<br>
selenium<br>

命令行执行可以生成测试报告——HTMLTestRunner<br>
记得测试类test.py前要导入：<br>
`import sys`<br>
`import os`<br>
`sys.path.append(os.path.join(os.path.dirname(__file__),".","."))`

手动编写页面对象<br>
## package petclinic-zd<br>
使用配置文件动态生成页面PageObject<br>
Page Factory(页面工厂)+配置文件(yaml)->PageObject
https://blog.csdn.net/weixin_33742618/article/details/90907731<br>
我认为这个分的太细化，不过是一种很好的思路<br>

##要获取导航图，就要获取当前module下所有类的列表<br>
### 见package petclinic.page
    clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    nodes = []
    # print(clsmembers)
    for class_name in clsmembers:
        if class_name[0].endswith('Page'):
            # print(class_name[0])
            nodes.append(class_name[0])
    # print(nodes)

## 获取每个node下的出边，即每个Page类下所包含的方法<br>
### 见package petclinic.page<br>
    for page in nodes:
        funmembers = inspect.getmembers(eval(page),inspect.isfunction)
        # print(funmembers)
        dic = {}
        edges = []
        for func in funmembers:
            if func[0] != '__init__':
                edges.append(func[0])
            dic[page]=edges
        print(dic)
结果：
    {'AddOwnerPage': ['add_owner']}<br>
    {'AddPetPage': ['add_pet']}<br>
    {'AddVisitPage': ['add_date']}<br>
    {'EditOwnerPage': ['edit_address', 'edit_city', 'edit_firstname', 'edit_lastname', 'edit_telephone']}<br>
    {'EditPetPage': ['edit_birth_date', 'edit_pet_name']}<br>
    {'FindOwnersPage': ['check_invalid_lastname_message', 'find_lastname']}<br>

再加一句获取参数，今天真是涨姿势

            for func in funmembers:
            if func[0] != '__init__':
                edges.append(func[0])
                params = inspect.getfullargspec(getattr(eval(page),func[0]))
                print(params[0])
            dic[page]=edges
好吧，Python中果然一切皆字典，最终版！！！<br>

    if __name__ == '__main__':
    clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    nodes = []
    for class_name in clsmembers:
        if class_name[0].endswith('Page'):
            # print(class_name[0])
            nodes.append(class_name[0])
    # 一定要把字典定义在循环外，不然生成的就是小字典！！！
    dic = {}
    dic_param = {}
    for page in nodes:
        funmembers = inspect.getmembers(eval(page),inspect.isfunction)
        # print(funmembers)
        edges = []
        for func in funmembers:
            if func[0] != '__init__':
                edges.append(func[0])
                # print(edges)
                params = inspect.getfullargspec(getattr(eval(page),func[0]))
                # print(params[0][1:])
                list = params[0][1:]
                dic_param[func[0]]=list
                dic[page]=edges
    print(dic_param)
    print(dic)
        

结果

    {'add_owner': ['firstName', 'lastName', 'address', 'city', 'telephone'], 'add_pet': ['name', 'birthDate'], 'add_date': ['date', 'description'], 'edit_address': ['address'], 'edit_city': ['city'], 'edit_firstname': ['firstName'], 'edit_lastname': ['lastName'], 'edit_telephone': ['telephone'], 'edit_birth_date': ['birthDate'], 'edit_pet_name': ['name'], 'check_invalid_lastname_message': [], 'find_lastname': ['lastname'], 'find_list': [], 'list_detail': []}
    {'AddOwnerPage': ['add_owner'], 'AddPetPage': ['add_pet'], 'AddVisitPage': ['add_date'], 'EditOwnerPage': ['edit_address', 'edit_city', 'edit_firstname', 'edit_lastname', 'edit_telephone'], 'EditPetPage': ['edit_birth_date', 'edit_pet_name'], 'FindOwnersPage': ['check_invalid_lastname_message', 'find_lastname', 'find_list'], 'OwnersListPage': ['list_detail']}

## 导航到下一个页面，使整个测试更加完整，而并不是执行每一个unittest测试<br>
还记得Page Object的最佳实践嘛？<br>
就是一个页面对象的导航方法返回下一个页面对象，这样就顺了
    
    class FindOwnersPage():
        def find_list(self):
        self.driver.find_element(*Locators.FIND_BUTTON).click()
        return OwnersListPage(self.driver)

    class OwnersListPage():

    def __init__(self,driver):
        self.driver = driver

    def list_detail(self):
        table = self.driver.find_element(*Locators.TABLE_LOC)
        rows = table.find_elements_by_tag_name("tr")
        rowname = []
        for row in rows[1:]:
            col = row.find_element_by_xpath("td[1]/a")
            rowname.append(col.text)
        return rowname
        
测试用例介么写

     def test_find_owner(self):
        driver = self.driver
        driver.get('http://localhost:8080/owners/find')
        find_page = FindOwnersPage(driver)
        list_page = find_page.find_list()
        list = list_page.list_detail()
        print(list)
        assert 'Betty Davis' in list
        
unittest跳过某个测试用例

    # 在测试用例前加这个
    @unittest.skip(u"强制跳过示例")
    
来到最激动人心的时刻，我想实现读取yaml文件或者字典，自动生成unittest的测试用例，
这样也方便后续导航路径的转化，减少手工操作，经过一番调研，准备采用jinja2模板<br>
所以在文件中增加一个自动生成测试用例的模板类的中间层Layer.py<br>
v0.1<br>
模板类testcase.j2<br>

    def test_{{ tc_name }}(self):
        driver = self.driver
        driver.get('{{ url }}')
        current_page = {{ current_page }}(driver)
        current_page.{{ func_name }}{{ params }}
        time.sleep(2)
Layer.py<br>

    """
    自动生成testcase的模板
    """
    from jinja2 import Template
    from jinja2 import Environment,PackageLoader
    env = Environment(loader=PackageLoader('petclinic'))
    template = env.get_template('testcase.j2')
    content = template.render(tc_name='add_owner',url='http://localhost:8080/owners/new',\
                              current_page='AddOwnerPage',func_name='add_owner',\
                              params='zheng')
    print(content)
    with open('./test_add_owner.py','w') as fp:
        fp.write(content)
        
这个其中还学习了一个pycharm代码回滚操作
https://blog.csdn.net/hfutdog/article/details/81711973<br>
LocalHistory -> revert<br>
jinja2中文文档 http://docs.jinkan.org/docs/jinja2/templates.html<br>

### 小试牛刀以后我们利用父子模板的继承关系自动生成整个test.py文件<br>
定义基本模板base.j2<br>
加入子模版的块

    {%  block testcase %}
    {%- endblock %}
    # -是为了去除空格，然而发现没有什么卵用
    
最后一步，读取前导航图，生成没有断言的测试用例<br>
## 自动生成Page Object类
### 现有工具
OHMAP——产生的是java类，主要是服务端代码静态分析，采用FirePath<br>
http://ohmap.virtuetech.de/<br>
SWD Page Recorder——允许用户运行Web应用并检测GUI元素，并且可以导出成多种语言代码<br>
https://github.com/dzharii/swd-recorder<br>
WTF PageObject Utility Chrome Extension——可以创建PO对象，通过类型：id,name,CSS,XPATH,并且输出为Python<br>
https://github.com/wiredrive/wtframework/wiki/WTF-PageObject-Utility-Chrome-Extension<br>
## 大论文思路点
1.PageObject生成，粗略生成，人工筛选——使用代码模板生成<br>
细粒度生成——运用Web数据挖掘或者页面聚类<br>
**2.测试序列生成——贪婪算法+广度优先树遍历算法**<br>
**3.测试数据生成PICT+Faker保证路径覆盖率**<br>

