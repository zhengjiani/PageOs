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