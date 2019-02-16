## Py2exe 安装使用说明

### 一、安装
1. 登陆py2exe官方网站http://www.py2exe.org/，下载对应python版本的安装程序，注意您使用的是32位版本还是64位版本的python。
2. Py2exe支持python2和python3，我将分别使用python2.7和python3.4演示命令行软件和tkinter桌面软件的打包方法。（py2exe仅支持python3.4以下版本）
### 二、生成exe文件
1. 编写您软件的源代码
2. 在软件的入口文件同级目录下，新建一个python文件，输入配置参数。
3. 在命令行中键入python xxx.py(配置文件) py2exe即可进行打包
### 三、修复中文显示错误
1. 写一个名为sitecustomize.py的文件，把它放在Python27下的Lib下site-packages目录中。	sitecustomize.py是一个特殊的文件，Python在启动时会自动导入它。该文件中的语句同时会执行。在sitecustomize.py中的语句sys.setdefaultencoding('UTF-8')的作用是将默认编码设置为UTF-8，这样使用中文时就不会出现UnicodeError错误。sitecustomize.py示例如下：
```python
#!/usr/bin/python
import sys
sys.setdefaultencoding('UTF-8')
```
2. py2exe的打包时中文乱码问题解决方案，如果你使用了sitecustomize.py文件，那么如果你的源程序中含有中文，则打包时要在源程序中加上import sitecustomize这句。
3. 在每个含有中文的py文件中的开头加上#-*- encoding:UTF-8 -*-
4. 将需要打包的源文件内的中文输出和输入全部改写为以下的格式:  
#### 输出​
```python
print unicode('成功:','utf-8')     
print unicode(strName,'utf-8')      #strName 是字符串     
```
#### 输入​
```python
n=raw_input(unicode('请输入文字','utf-8').encode('gbk'))   
```

### 参考文献：
```
http://blog.sina.com.cn/s/blog_6360da6a0102y2nv.html
http://www.py2exe.org/
```
