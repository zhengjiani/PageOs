## 解析java类
即解析生成的PO类的java文件<br>
将java文件——>txt文件——>读取文件，首先解析出@FindBy中的CSS元素
## 自动生成PageObject对象
class name -> 解析Web页面的URL<br>
web elements of interest for web testing -> 变量名<br>
使用Page Factory模式自动创建构造器，构造器初始化web元素类和webDrivers实例<br>
all the menu bar links in the page -> navigational methods
>(1) WebElement instances for each ‘‘clickable’’ element (i.e., an element on which it is possible to perform an action, e.g., links, buttons, input ﬁelds); <br>
>(2) methods to navigate the aforementioned graph structure;<br>
>(3)  methods to ﬁll and submit forms. 

因为我要遍历列表，然后我就在模板生成的文件中作循环，结果一直生成多次，其实应该在jinja2模板中循环变量，如下<br>
去空格+迭代

    {% extends 'base.j2' %}
    {%  block locators -%}
        {{ super() }}
        {%- for loc_name,link_name in dic_link.items()  -%}
        {{ loc_name }} = (By.LINK_TEXT,'{{ link_name }}')
        {% endfor %}
    {%-  endblock %}
   
# pandas聚合、分组、统计操作
删除字典中重复值对应的键

    func = lambda z:dict([(x, y) for y, x in z.items()])
    print(len(func(func(res1))))
    上述方法等同于
    lis =set()
    for k,v1 in res1.items():
        for k2,v2 in res1.items():
            if v1 == v2:
                lis.add(v1)
    print(len(lis))