# -*- encoding: utf-8 -*-
"""
@File    : gen_testcase.py
@Time    : 2020/3/30 7:28 下午
@Author  : zhengjiani
@Email   : 936089353@qq.com
@Software: PyCharm
"""
from jinja2 import Environment,  FileSystemLoader

class gen_test:
    """根据Jinja2模版 + 路径生成测试用例"""
    def generate(self,pathlists):
        """
        :param pathlists: 测试路径列表
        示例：
        pathlists = [
                '<\HomePage:goto_search,FindPage:goto_detail_page,DetailPage>',
                '<\HomePage:goto_search,FindPage:goto_detail_page,DetailPage>',
                '<\HomePage:goto_search,FindPage:goto_detail_page,DetailPage:goto_edit_pet,PetPage:edit_pet(R1),DetailPage>',
                '<\HomePage:goto_search,FindPage:goto_detail_page,DetailPage:goto_visit,AddNewVisitPage:add_visit(R1),DetailPage>',
                '<\HomePage:goto_search,FindPage:goto_detail_page,DetailPage:goto_edit,EditOwnerPage:edit_info(R1),DetailPage>',
                '<\HomePage:goto_register,RegisterPage:regist_owner(R2),ErrorMsg>',
                '<\HomePage:goto_register,RegisterPage:regist_owner(R1),FindPage:goto_detail_page,DetailPage>',
                '<\HomePage:goto_Veter,VeterPage>'

            ]
        :return: 生成文件
        """
        env = Environment(loader=FileSystemLoader("/Users/zhengjiani/PycharmProjects/PageOs_v0.1/gen_test/templates"))
        template = env.get_template("testcase.j2")

        path = []
        methods = []
        pages = set()
        for item in pathlists:
            print(item)
            path.append(item[1:][:-1].split(','))
        for item in path:
            method = {}
            for i in item:
                if ':' in i:
                    pages.add(i.split(':')[0])
                    method[i.split(':')[0]]= i.split(':')[1]
                if i.endswith('Page'):
                    pages.add(i)
            methods.append(method)



        content = template.render(pathlists=path,pages = list(pages),methods=methods,type=type)

        with open('/Users/zhengjiani/PycharmProjects/PageOs_v0.1/gen_test/path_test.py','w') as fp:
            fp.write(content)

if __name__ == '__main__':
    pathlists = [
        "<HomePage:goto_search,FindPage:goto_detail_page,DetailPage>",
        "<HomePage:goto_search,FindPage:goto_detail_page,DetailPage>",
        "<HomePage:goto_search,FindPage:goto_detail_page,DetailPage:goto_edit_pet,PetPage:edit_pet(R1),DetailPage>",
        "<HomePage:goto_search,FindPage:goto_detail_page,DetailPage:goto_visit,AddNewVisitPage:add_visit(R1),DetailPage>",
        "<HomePage:goto_search,FindPage:goto_detail_page,DetailPage:goto_edit,EditOwnerPage:edit_info(R1),DetailPage>",
        "<HomePage:goto_register,RegisterPage:regist_owner(R2),ErrorMsg>",
        "<HomePage:goto_register,RegisterPage:regist_owner(R1),FindPage:goto_detail_page,DetailPage>",
        "<HomePage:goto_Veter,VeterPage>"

    ]
    g = gen_test()
    g.generate(pathlists=pathlists)