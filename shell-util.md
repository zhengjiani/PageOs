画图命令
```dot -Tpng petclinic.txt -o petclinic.png ```

RTED_v1.2.jar # Calculation tree distance
page_generator.sh # call selenium page object generator

为启动文件manage.py加权限

     chmod u+rwx manage.py 
     
数据库创建与删除

    python3 manage.py shell
    >>> db.create_all()
    >>> db.drop_all()
    

    
改动数据库以后执行迁移操作

    python manage.py db migrate -m "modify info"
    
    # 输出的信息包含改动的字段
    ~/PycharmProjects/PageOs_v0.1(v1*) » python manage.py db migrate -m "add page model"                            zhengjiani@zhengjianideMacBook-Pro
    INFO  [alembic.runtime.migration] Context impl MySQLImpl.
    INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
    INFO  [alembic.autogenerate.compare] Detected added table 'pages'
    INFO  [alembic.autogenerate.compare] Detected added index 'ix_pages_pagename' on '['pagename']'
    Generating /Users/zhengjiani/PycharmProjects/PageOs_v0.1/migrations/versions/6d2cdd0601cf_add_page_model.py ...  done

    # 更新数据库
    ~/PycharmProjects/PageOs_v0.1(v1*) » python manage.py db upgrade                                                zhengjiani@zhengjianideMacBook-Pro
    INFO  [alembic.runtime.migration] Context impl MySQLImpl.
    INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
    INFO  [alembic.runtime.migration] Running upgrade 8d32dac5d61e -> 6d2cdd0601cf, add page model

数据库回滚
- 获取 History ID
`python manage.py db history`

- 回滚到某个 history
`python manage.py db downgrade <history_id>`

- 获取列表中重复元素索引值

```
    ans = np.where(np.array(po_queue) == item)
    deque(['AddNewPetPage', 'EditOwnerPage', 'PetPage', 'PetPage', 'AddNewVisitPage', 'DetailPage', 'DetailPage', 'DetailPage'])
    (array([2, 3]),)
```

- Flask阿里云部署启动方式
    `gunicorn -w 4 -b 0.0.0.0:5000 manage:app`

- Jinja2模版写法

执行for循环和打印结果
```jinja2
{% for item in navigation %}
        <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
{% endfor %}
```
变量
```jinja2
{{ foo.bar }}
{{ foo['bar'] }}
```
过滤器
```jinja2
{{ name|striptags|title }} # 移除 name 中的所有 HTML 标签并且改写 为标题样式的大小写格式。
{{ list|join(', ') }} # 把一个列表用逗号连接起来
```
判断一个值是否定义过
```jinja2
{{name is defined }} # 根据返回true/false
```
空白控制，移除前/后空格
```jinja2
{% for item in seq -%}
    {{ item }}
{%- endfor %}
```
转义/展示Jinja2语法
```jinja2
{{ '{{' }}
{% raw %}
    <ul>
    {% for item in seq %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>
{% endraw %}
```
行语句
```jinja2
# for item in seq:
    ...
# endfor
```
模版继承
base.html
```jinja2
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="en">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    {% block head %}
    <link rel="stylesheet" href="style.css" />
    <title>{% block title %}{% endblock %} - My Webpage</title>
    {% endblock %}
</head>
<body>
    <div id="content">{% block content %}{% endblock %}</div>
    <div id="footer">
        {% block footer %}
        &copy; Copyright 2008 by <a href="http://domain.invalid/">you</a>.
        {% endblock %}
    </div>
</body>
```
子模版
```jinja2
{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
    {{ super() }}
    <style type="text/css">
        .important { color: #336699; }
    </style>
{% endblock %}
{% block content %}
    <h1>Index</h1>
    <p class="important">
      Welcome on my awesome homepage.
    </p>
{% endblock %}
```
控制结构
```jinja2
{% for user in users %}
  <li>{{ user.username|e }}</li>
{% endfor %}
{% for key, value in my_dict.iteritems() %}
    <dt>{{ key|e }}</dt>
    <dd>{{ value|e }}</dd>
{% endfor %}
```
特殊变量
```jinja2
变量	描述
loop.index	当前循环迭代的次数（从 1 开始）
loop.index0	当前循环迭代的次数（从 0 开始）
loop.revindex	到循环结束需要迭代的次数（从 1 开始）
loop.revindex0	到循环结束需要迭代的次数（从 0 开始）
loop.first	如果是第一次迭代，为 True 。
loop.last	如果是最后一次迭代，为 True 。
loop.length	序列中的项目数。
loop.cycle	在一串序列间期取值的辅助函数。见下面的解释。
```
列表中选择取值
```jinja2
{% for row in rows %}
    <li class="{{ loop.cycle('odd', 'even') }}">{{ row }}</li>
{% endfor %}
```
如果因序列是空或者过滤移除了序列中的所有项目而没有执行循环，你可以使用 else 渲染一个用于替换的块:
```jinja2
<ul>
{% for user in users %}
    <li>{{ user.username|e }}</li>
{% else %}
    <li><em>no users found</em></li>
{% endfor %}
</ul>
```
递归数据
```jinja2
<ul class="sitemap">
{%- for item in sitemap recursive %}
    <li><a href="{{ item.href|e }}">{{ item.title }}</a>
    {%- if item.children -%}
        <ul class="submenu">{{ loop(item.children) }}</ul>
    {%- endif %}</li>
{%- endfor %}
</ul>
```
宏，把常用行为作为可重用函数，取代手动重复工作
```jinja2
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{
        value|e }}" size="{{ size }}">
{%- endmacro %}
<p>{{ input('password', type='password') }}</p>
```
