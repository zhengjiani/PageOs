##pageOs_v0.1 

PageOs_v0.1

    ├── bokchoy_pages  # page object files
    ├── faker_data     # MOCK data
    ├── resources      # Flask-blueprint
    ├── similar_analysis # web page similar analysis
    ├── test-output # .dot/.png files
    ├── test_gen # testcases generate
    ├── uploads # save upload file
    
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
    
运行方式 

    python3 manage.py runserver
    
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
# 获取 History ID
python manage.py db history

# 回滚到某个 history
python manage.py db downgrade <history_id>

# 获取列表中重复元素索引值
    ans = np.where(np.array(po_queue) == item)
    
    deque(['AddNewPetPage', 'EditOwnerPage', 'PetPage', 'PetPage', 'AddNewVisitPage', 'DetailPage', 'DetailPage', 'DetailPage'])
    (array([2, 3]),)
    
### Flask阿里云部署启动方式

    gunicorn -w 4 -b 0.0.0.0:5000 manage:app
