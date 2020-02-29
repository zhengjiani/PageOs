PageObject编写规范：

Generally, this is the right behavior. However, at times it
    will be useful to not verify the page before executing a method.
    In those cases, the method can be marked with the :func:`unguarded`
    decorator. Additionally, private methods (those beginning with `_`)
    are always unguarded.
    
通常页面对象都是经过验证后才可以执行的方法，如果要使用不经过页面验证就执行的方法可以通过装饰器标识
```
    @unguarded
    def method_1(self):
        self.q().click()
```
类或者实例属性的标识方法
```
    @property
    @unguarded
    def foo(self):
        return self._foo
```
api:

is_browser_on_page  

求一个矩阵中最大的元素

```
#找到距离最大的下标
def find_max(M):
    max = 0
    x = 0
    y = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            if i != j and M[i][j] > max:
                max = M[i][j]
                x = i
                y = j
    return (x, y, max)
```
TOP_K 问题
```
# # 求最大相似度的K个索引
        res1 = map(M.index, heapq.nlargest(k, M))
        # # print(list(res1))
        # # 求最大K个元素
        re2 = heapq.nlargest(k, M)
        for i in list(res1):
            print(C[i])
        print(re2)
```