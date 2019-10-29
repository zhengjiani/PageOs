# PageOs
我的实验

上传文件代码

    # -*- coding: utf-8 -*-
    # @Time    : 2019/6/3 14:30
    # @Author  : zhengjiani
    # @Software: PyCharm
    # @Blog    ：https://zhengjiani.github.io/
    import os
    import os
    from flask import Flask, flash, request, redirect, url_for
    from werkzeug.utils import secure_filename
    from flask import send_from_directory
    
    UPLOAD_FOLDER = '/Users/zhengjiani/PycharmProjects/PageOs_latest/files'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'py'}
    
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
    
    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'],
                                   filename)
    @app.route('/', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('uploaded_file',
                                        filename=filename))
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
        '''
    if __name__ == '__main__':
        app.run()

官方打包指南

    pip install -e .
    这个命令告诉 pip 在当前文件夹中寻找 setup.py 并在 编辑 或 开发 模式下安装。编辑模式是指当改变本地代码后，只需要重新项目。比如改变了项目 依赖之类的元数据的情况下。
    pip list