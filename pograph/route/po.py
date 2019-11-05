import os
from flask import (
    Blueprint,flash,g,redirect,render_template,request,url_for,current_app
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
from flask import send_from_directory

from pograph.route.auth import login_required
from pograph.db import get_db
from pograph.common.model import Tester,Po,db
from pograph.common.forms import TesterForm
bp = Blueprint('po',__name__)


ALLOWED_EXTENSIONS = {'py','txt'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'],filename)


# 索引页会显示所有的帖子
@bp.route('/',methods=['GET','POST'])
def index():
    # 创建自定义表单类
    tester_form = TesterForm()
    '''
    验证逻辑
    1.调用WTF的函数实现验证
    2.验证通过获取数据
    3.判断测试人员是否存在
    4.如果测试人员存在，判断页面对象是否存在，没有重复页面对象就添加数据，如果重复就提示错误
    5.如果测试人员不存在，添加测试人员和页面对象
    6.验证不通过就提示错误
    '''
    # 调用WTF的函数实现验证
    if tester_form.validate_on_submit():
        # 验证通过获取数据
        tester_name = tester_form.tester.data
        po_name = tester_form.po.data

        # 判断测试人员是否存在
        tester = Tester.query.filter_by(name=tester_name).first()
        # 如果测试人员存在
        if tester:
            # 判断页面对象是否存在，
            po = Po.query.filter_by(name=po_name).first()
            # 如果重复就提示错误
            if po:
                flash('已存在同名页面对象')
            # 没有重复页面对象就添加数据，
            else:
                try:
                    new_po = Po(name=po_name,tester_id=tester.id)
                    db.session.add(new_po)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    flash('添加书籍失败')
                    db.session.rollback()
        else:
            # 如果测试人员不存在
            try:
                new_tester = Tester(name=tester_name)
                db.session.add(new_tester)
                db.session.commit()
                new_po = Po(name=po_name,tester_id=new_tester.id)
                db.session.add(new_po)
                db.session.commit()
            except Exception as e:
                print(e)
                flash('添加作者和书籍失败')
                db.session.rollback()

    else:
        # 验证不通过就提示错误
        if request.method == 'POST':
            flash('参数不全')

    # 查询所有的tester信息，将数据传递给模版
    testers = Tester.query.all()
    pos = Tester.pos
    return render_template('po/index.html',testers=testers,form=tester_form)
# 删除测试人员
@bp.route('/delete_tester/<tester_id>')
def delete_tester(tester_id):
    # 查询数据库，是否有该id的测试人员，如果有就删除(先删除页面对象再删测试人员)，没有就提示错误
    tester = Tester.query.get(tester_id)
    if tester:
        try:
            # 查询之后直接删除
            Po.query.filter_by(tester_id=tester.id).delete()
            # 删除作者
            db.session.delete(tester)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除测试人员出错')
            db.session.rollback()
    else:
        flash('测试人员找不到')
    return redirect(url_for('index'))
# 删除页面对象
@bp.route('/delete_po/<po_id>')
def delete_po(po_id):
    # 查询数据库，是否有该id的页面对象，如果有就删除，没有就提示错误
    po = Po.query.get(po_id)
    # 如果有就删除
    if po:
        try:
            db.session.delete(po)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除书籍出错')
            db.session.rollback()
    else:
        # 没有提示错误
        flash('页面对象找不到')

    # 如何返回当前网址，重定向
    # return redirect('www.baidu.com')
    # return redirect('/')
    # redirect:重定向，重新传入网络/路由地址
    # url_for('index'):需要传入视图函数名，返回该视图函数对应的路由地址
    return redirect(url_for('index'))
# 上传pageobject.py文件
@bp.route('/upload',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('没有选择文件')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'],filename))
            return redirect(url_for('po.uploaded_file',filename=filename))
    return render_template('upload.html')

# 导航图详情页
@bp.route('/pos/<name>',methods=['GET'])
def pos(name):
    pass
# # 创建
# @bp.route('/create',methods=('GET','POST'))
# @login_required
# def create():
#     if request.method == 'POST':
#         title = request.form['title']
#         body = request.form['body']
#         error = None
#
#         if not title:
#             error = 'Title is required.'
#
#         if error is not None:
#             flash(error)
#
#         else:
#             db = get_db()
#             db.execute(
#                 'INSERT INTO post (title,body,author_id)'
#                 'VALUES (?,?,?)',
#                 (title,body,g.user['id'])
#             )
#             db.commit()
#             return redirect(url_for('po.index'))
#     return render_template('po/create.html')
#
# def get_post(id, check_author=True):
#     post = get_db().execute(
#         'SELECT p.id, title, body, created, author_id, username'
#         ' FROM post p JOIN user u ON p.author_id = u.id'
#         ' WHERE p.id = ?',
#         (id,)
#     ).fetchone()
#
#     if post is None:
#         abort(404, "Post id {0} doesn't exist.".format(id))
#
#     if check_author and post['author_id'] != g.user['id']:
#         abort(403)
#
#     return post
# # 更新
# @bp.route('/<int:id>/update',methods=('GET','POST'))
# @login_required
# def update(id):
#     post = get_post(id)
#
#     if request.method == 'POST':
#         title = request.form['title']
#         body = request.form['body']
#         error = None
#
#         if not title:
#             error = 'Title is required.'
#
#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             db.execute(
#                 'UPDATE post SET title = ?,body = ?'
#                 'WHERE id = ?',
#                 (title,body,id)
#             )
#             db.commit()
#             return redirect(url_for('po.index'))
#     return render_template('po/update.html',post=post)
#
# # 删除
# @bp.route('/<int:id>/delete',methods=('POST',))
# @login_required
# def delete(id):
#     get_post(id)
#     db = get_db()
#     db.execute('DELETE FROM post WHERE id = ?',(id,))
#     db.commit()
#     return redirect(url_for('po.index'))