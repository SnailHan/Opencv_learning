# Opencv_learning这是一个 opencv的学习的个人库， 安装配置环境请查看下面的文档
windows_python2.7_opencv3.2
https://github.com/wjb711/Opencv_learning/blob/master/windows_python2.7_opencv3.2


目前刚写了  一个转换动画片彩色图片到黑白图片的儿童绘本的脚本， 以后慢慢写， 慢慢更新
win7+python3.6+opencv3.2+contrib
推荐python 用新的3.5  32位，为什么是32位？因为我的电脑就是32位的系统
为什么不是2.7？ 因为opencv contrib 包只支持3.5 3.6
为什么不是最新的3.6？ 因为我准备研究dlib，一个关于人脸的模块，目前仅支持到3.5
python3.5下载地址
https://www.python.org/downloads/release/python-353/
选择“Windows x86 executable installer”

安装完成python3.5后，先安装numpy
pip install numpy
或者下载“numpy‑1.12.1+mkl‑cp35‑cp35m‑win32.whl”
http://www.lfd.uci.edu/~gohlke/pythonlibs/

再安装opencv+contrib
opencv_python‑3.2.0+contrib‑cp35‑cp35m‑win32.whl
http://www.lfd.uci.edu/~gohlke/pythonlibs/

最后安装dlib
https://pypi.python.org/pypi/dlib/18.17.100
选择dlib-18.17.100-cp35-none-win32.whl (md5)
关于dlib的用法
请看这位牛人博客
http://www.pyimagesearch.com/

py -2 -m pip install XXXX


-2 还是表示使用 Python2，-m pip 表示运行 pip 模块，也就是运行pip命令了。如果是为Python3安装软件，那么命令类似的变成


py -3 -m pip install XXXX






两个安装python软件包的地址

https://pypi.python.org/pypi/
http://www.lfd.uci.edu/~gohlke/pythonlibs/


python上的Gui, easygui
安装方法：
pip install easygui
用法1
import easygui
easygui.msgbox('hello world')

用法2
from easygui import msgbox, multenterbox

fieldNames = ["Name"]
fieldValues = list(multenterbox(msg='Fill in values for the fields.', title='Enter', fields=(fieldNames)))
msgbox(msg=(fieldValues), title = "Results")
print (fieldValues)

用法3
import easygui
image = "3.jpg"
msg = "Do you like this picture?"
choices = ["Yes","No","No opinion"]
reply = easygui.buttonbox(msg, image=image, choices=choices)

更多用法
http://easygui.sourceforge.net/tutorial.html



pip 在win7 下更改国内的源
C:\Users\%username%\AppData\Local\pip
手动建pip.ini, 内容如下
[global] 
index-url = http://pypi.douban.com/simple/ 
trusted-host = pypi.douban.com 


python转exe的方法
先安装pyinstaller
pip install pyinstaller
生成exe的方法
pyinstaller yourfile.py
pyinstaller --onefile yourfile.py


pip install 在windows下始终因ascii报错UnicodeDecodeError
petanne petanne 2015-10-22 16:47:42
问题是使用pip install django 或其它时，始终报错：
UnicodeDecodeError: 'ascii' codec can't decode byte 0xb1 inposition 34: ordinal
not in range(128)

原因是windows的cmd环境默认为gbk编码，pip默认用utf8编码。
在Linux和Mac中，terminal环境默认的是utf8编码，所以不会报错。

解决方法：
python目录 Python27\Lib\site-packages 建一个文件sitecustomize.py 
内容为： 
import sys 
sys.setdefaultencoding('gbk') 
