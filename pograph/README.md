文件__init__.py

app = Flask(__name__, instance_relative_config=True) 创建 Flask 实例

instance_relative_config=True 告诉应用配置文件是相对于 instance folder 的相对路径。实例文件夹在 flaskr 包的外面，用于存放本地数据（例如配置密钥和数据库），不应当 提交到版本控制系统。
可以显式定义实例文件夹：
    
    app = Flask(__name__, instance_path='/path/to/instance/folder')
    # 提供的路径是绝对路径
    
运行应用

    $ export FLASK_APP=pograph
    $ export FLASK_ENV=development
    $ flask run
    
运行init-db命令

    $ flask init-db
    
视图是一个应用对请求进行响应的函数。 Flask 通过模型把进来的请求 URL 匹配到 对应的处理视图。视图返回数据， Flask 把数据变成出去的响应。 Flask 也可以反 过来，根据视图的名称和参数生成 URL 。

蓝图方式是把它们注册到蓝图，然后在工厂函数中 把蓝图注册到应用。

为了更好地管理文件，属于某个蓝图 的模板会被放在与蓝图同名的文件夹内。

除了 CSS ，其他类型的静态文件可以是 JavaScript 函数文件或者 logo 图片。它们 都放置于 flaskr/static 文件夹中，并使用 url_for('static', filename='...') 引用。

当你完成每个视图时，请保持开发服务器运行。当你保存修改后，请尝试在浏览器中 访问 URL ，并进行测试。

loop.last 是一个 Jinja for 循环 内部可用的特殊变量，它用于在每个 博客帖子后面显示一条线来分隔帖子，最后一个帖子除外