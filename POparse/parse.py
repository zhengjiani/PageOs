# -*- coding: utf-8 -*-
# @Time    : 2019/6/19 10:09
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
# 去掉文件中的注释
def removeComments(source):
    in_block = False
    ans = []
    for line in source:
        i = 0
        if not in_block:
            newline = []
        while i < len(line):
            if line[i:i + 2] == '/*' and not in_block:
                in_block = True
                i += 1
            elif line[i:i + 2] == '*/' and in_block:
                in_block = False
                i += 1
            elif not in_block and line[i:i + 2] == '//':
                break
            elif not in_block:
                newline.append(line[i])
            i += 1
        if newline and not in_block:
            ans.append("".join(newline))
    return ans
# 将处理后的文本写入文件中
def writeoutputfile(ans):
    fileObject = open('output.txt', 'w')
    for line in ans:
        fileObject.write(line)
        fileObject.write('\n')
    fileObject.close()
# 去除java中的import和空格文件
def removeimport(ans):
    result = []
    for i in ans:
        if not i.startswith('i'):
            if i.strip() != '':
                result.append(i.strip())
    return result
# 找出所有定位
def locate(ans):
    findby = []
    for i in ans:
        if i.startswith('@FindBy'):
            findby.append(i)
    return findby
f = open('findpage.java','r')
source = f.readlines()
ans = removeComments(source)
lis = removeimport(ans)
print(locate(lis))
# print(ans)
