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
    
# 解析html文件，聚类网页
TF——Tag List 获取标签列表，统计每一个标签出现的频率<br>
python保留两位小数
    
    a_tf = Decimal(len(a_list)/tag_total).quantize(Decimal('0.00'))
去除停用词的方法参考——https://www.geeksforgeeks.org/removing-stop-words-nltk-python/

    # simple的例子
    from nltk.corpus import stopwords 
    from nltk.tokenize import word_tokenize 
    example_sent = "This is a sample sentence, showing off the stop words filtration."
    stop_words = set(stopwords.words('english')) 
    word_tokens = word_tokenize(example_sent) 
    filtered_sentence = [w for w in word_tokens if not w in stop_words] 
    filtered_sentence = [] 
    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w) 
    print(word_tokens) 
    print(filtered_sentence) 
项目中使用的是从文件中读取的方式<br>
分割字符串https://blog.csdn.net/doiido/article/details/43204675<br>

    #使用默认分隔符
    >>> print u.split()
    ['www.doiido.com.cn']
 
    #以"."为分隔符
    >>> print u.split('.')
    ['www', 'doiido', 'com', 'cn']
 
    #分割0次
    >>> print u.split('.',0)
    ['www.doiido.com.cn']
 
    #分割一次
    >>> print u.split('.',1)
    ['www', 'doiido.com.cn']
 
    #分割两次
    >>> print u.split('.',2)
    ['www', 'doiido', 'com.cn']
 
    #分割两次，并取序列为1的项
    >>> print u.split('.',2)[1]
    doiido
 
    #分割最多次（实际与不加num参数相同）
    >>> print u.split('.',-1)
    ['www', 'doiido', 'com', 'cn']
 
    #分割两次，并把分割后的三个部分保存到三个文件
    >>> u1,u2,u3 = u.split('.',2)
    >>> print u1
    www
    >>> print u2
    doiido
    >>> print u3
    com.cn

    2、去掉换行符
    >>> c = '''say
    hello
    baby'''
 
    >>> print c
    say
    hello
    baby
 
    >>> print c.split('\n')
    ['say', 'hello', 'baby']
获取所有文本

    if soup.a.get_text() is not None:
    a_texts=soup.a.get_text(",",strip=True).split(',')
    print(a_texts)
git 统计代码行数

    find . "(" -name "*.java" ")" -print | xargs wc -l
    
计算字串相似度（字符串编辑距离）`pip install python-Levenshtein`
https://www.cnblogs.com/kaituorensheng/archive/2013/05/18/3085653.html<br>
在下面网址下载.whl文件https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-levenshtein<br>
使用命令——pip install python_Levenshtein-0.12.0-cp37-cp37m-win_amd64.whl<br>

移除标签tag的内容<br>

    markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
    soup = BeautifulSoup(markup,'html.parser')
    markup=soup.i.clear()
    print(soup.a)
    
计算树编辑距离`pip install zss`
### Python数据类型转换（str跟int的转换）
字符串str转换为int: int_value = int(str_value)</br>
python运行命令行命令，我用来调用jar包</br>

    import os
    os.chdir("D:\\code\\python\\PageOs")
    print(os.system('java -jar RTED_v1.2.jar -t {a{b}{c}} {a{b{d}}} -o -v'))
输出结果：
    
    distance:             2.0
    runtime:              0.0
    relevant subproblems: 12
    recurence steps:      2
    left paths:           2
    right paths:          0
    heavy paths:          0
    
python按行读取文件：<br>

    https://www.cnblogs.com/xuxn/archive/2011/07/27/read-a-file-with-python.html
    
数据集网址：https://pythonprogramming.net/static/downloads/machine-learning-data/titanic.xls
新的模块sklearn.model_selection，将以前的sklearn.cross_validation, sklearn.grid_search 和 sklearn.learning_curve模块组合到一起<br>

通过指定标签名称和相应的轴，或直接指定索引或列名称来删除行或列。 使用多索引时，可以通过指定级别来删除不同级别上的标签。<br>

    X = np.array(df.drop([''],1).astype(float))
    
矩阵输入模式
Numpy.ndarray
NumPy 最重要的一个特点是其 N 维数组对象 ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。
ndarray 对象是用于存放同类型元素的多维数组。
ndarray 中的每个元素在内存中都有相同存储大小的区域。

    # print(np.ndarray)
    1,2,3
    (1, 2, 3)
    [1,2],[3,4]
    ([1, 2], [3, 4])
    
np.shape()
shape函数的功能是读取矩阵的长度，比如shape[0]就是读取矩阵第一维度的长度,相当于行数。
它的输入参数可以是一个整数表示维度，也可以是一个矩阵。shape函数返回的是一个元组，表示数组（矩阵）的维度
当数组只有一个维度的时候

    
    >>> a=np.array([1,2])
    >>> a
    array([1, 2])
    >>> a.shape
    (2L,)
    >>> a.shape[0]
    2L
    >>> a.shape[1]
    Traceback (most recent call last):
      File "<pyshell#63>", line 1, in <module>
        a.shape[1]
    IndexError: tuple index out of range   #最后报错是因为一维数组只有一个维度，可以用a.shape或a.shape[0]来访问
    ————————————————
    版权声明：本文为CSDN博主「雨落诗山山亦奇」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
    原文链接：https://blog.csdn.net/qq_38669138/article/details/79084275
当数组有两个维度
    
    >>> a=np.array([[1,2],[3,4]])    #注意二维数组要用（）和[]一起包裹起来，键入print a 会得到一个用2个[]包裹的数组（矩阵）
    >>> a
    array([[1, 2],
           [3, 4]])
    >>> a.shape
    (2L, 2L)
    >>> b=np.array([[1,2,3],[4,5,6]])
    >>> b
    array([[1, 2, 3],
           [4, 5, 6]])
    >>> b.shape
    (2L, 3L)

字典中键：数组、字符串、元祖
(stat1,stat2)
(stat1,stat3)
cluster = []
if d[(stat1,stat2)] > d[(stat1,stat3)]:
    new_vec = stat2
    cluster.append(stat2)
    del d[stat3]
    