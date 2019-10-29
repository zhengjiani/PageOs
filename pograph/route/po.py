import os
from flask import (
    Blueprint,flash,g,redirect,render_template,request,url_for,current_app
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
from flask import send_from_directory

from pograph.route.auth import login_required
from pograph.db import get_db
bp = Blueprint('po',__name__)


ALLOWED_EXTENSIONS = {'py','txt'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'],filename)


# 索引页会显示所有的帖子
# 主页为上传pageobject.py文件
@bp.route('/',methods=['GET','POST'])
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