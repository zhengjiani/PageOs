# pageOs_v0.1 
# 基于页面对象的WEB应用测试用例生成系统
声明：
该系统为本人毕业论文所设计的原型系统后端，采用Flask框架

[前端地址!](https://github.com/zhengjiani/Vue-po)

详细实现见**接口文档.md**

[小论文参见!](https://kns.cnki.net/KCMS/detail/detail.aspx?dbcode=CJFQ&dbname=CJFDLAST2020&filename=JSJY202001034&v=MTg2NzBITXJvOUdZSVI4ZVgxTHV4WVM3RGgxVDNxVHJXTTFGckNVUjdxZlkrUm9GeW5rV3I3Skx6N0JkN0c0SE4=)

思路启发论文：

[1] Biagiola M, Ricca F, Tonella P. Search based path and input data generation for web application testing[C].Proceedings of the 2016 International Symposium on Search Based Software Engineering. Cham: Springer, 2017, 18-32.

PageOs_V0.1

    ├── bokchoy_pages  # page object files
    ├── faker_data     # MOCK data
    ├── resources      # Flask-blueprint
    ├── similar_analysis # web page similar analysis
    ├── test-output # .dot/.png files
    ├── test_gen # testcases generate
    ├── uploads # save upload file
    
PageOs_V1.0

        .
    ├── app
    │   └── api
    ├── bokchoy_pages
    │   ├── pageKit
    │   │   ├── auto_po
    │   │   └── po
    │   └── phoenix
    ├── download
    ├── faker_data
    ├── gen_test
    │   └── templates
    ├── migrations
    │   └── versions
    ├── output
    ├── similar_analysis
    │   ├── csv_file
    │   ├── doms
    │   ├── doms_test
    │   ├── images
    │   └── templates
    ├── test
    └── uploads

运行方式 

    python3 manage.py runserver