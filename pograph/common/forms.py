# -*- encoding: utf-8 -*-
"""
@File    : forms.py
@Time    : 2019/11/5 5:19 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
# 自定义表单类
class TesterForm(FlaskForm):
    tester = StringField('测试人员',validators=[DataRequired()])
    po = StringField('页面对象',validators=[DataRequired()])
    submit = SubmitField('提交')