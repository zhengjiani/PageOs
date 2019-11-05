# -*- encoding: utf-8 -*-
"""
@File    : model.py
@Time    : 2019/10/28 4:57 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Nicezheng_1995@127.0.0.1:3306/flask_pos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 创建数据库对象
db = SQLAlchemy(app)
# 定义测试人员和页面对象模型
# 测试人员模型
class Tester(db.Model):
    # 表名
    __tablename__ = 'testers'
    # 字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    # 关系引用:pos是给自己用的，tester是给Po模型用的
    pos = db.relationship('Po', backref='tester')

    def __repr__(self):
        return 'Tester: %s' % self.name


# 页面对象模型
class Po(db.Model):
    __tablename__ = 'pos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    tester_id = db.Column(db.Integer, db.ForeignKey('testers.id'))

    def __repr__(self):
        return 'Po: %s %s' % (self.name, self.tester_id)
if __name__ == '__main__':
    # 删除表
    db.drop_all()
    # 创建表
    db.create_all()
    # python生成数据
    ts1 = Tester(name='dingcun')
    ts2 = Tester(name='hanxue')
    # 把数据提交给用户会话
    db.session.add_all([ts1,ts2])
    # 提交会话
    db.session.commit()
    po1 = Po(name='LoginPage',tester_id=ts1.id)
    po2 = Po(name='SearchPage',tester_id=ts1.id)
    po3 = Po(name='UserPage',tester_id=ts2.id)
    po4 = Po(name='AddressPage', tester_id=ts2.id)
    db.session.add_all([po1,po2,po3,po4])
    db.session.commit()





