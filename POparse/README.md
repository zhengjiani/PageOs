## 解析java类
即解析生成的PO类的java文件<br>
将java文件——>txt文件——>读取文件，首先解析出@FindBy中的CSS元素
## 自动生成PageObject对象
class name -> 解析Web页面的URL<br>
web elements of interest for web testing -> 变量名<br>
使用Page Factory模式自动创建构造器，构造器初始化web元素类和webDrivers实例<br>
all the menu bar links in the page -> navigational methods
>(1) WebElement instances for each ‘‘clickable’’ element (i.e., an element on which it is possible to perform an action, e.g., links, buttons, input ﬁelds); <br>
>(2) methods to navigate the aforementioned graph structure;<br>
>(3)  methods to ﬁll and submit forms. 