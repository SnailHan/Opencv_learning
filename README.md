# Opencv_learning
win7+python2.7+opencv3.2安装配置教程
论坛上都是opencv+vs的安装配置贴， 安装配置的过程令人崩溃

 我来写个傻瓜型的opencv+python的安装贴， 方便新人入门
OS：win7或win10均可， 32位，64位均可
python 建议用2.7版本系列的， 网上的教程呢也大多基于此系列版本， 为了减少调试中的不一致问题， 建议使用此版本
 当然32位的， 64位下的各种问题， 提出来也没人帮忙解决， 老老实实用python 2.7 32位 
 下载地址
https://www.python.org/downloads/windows/
 选
Windows x86 MSI installer

 建议安装到
C:\CV\Python27
安装完成后， 记得添加系统环境变量path中
手动添加windows的环境变量
C:\CV\Python27;C:\CV\Python27\Scripts
安装完成后安装numpy
DOS下用命令pip install numpy即可， 确保网络连接通畅
 接下来安装opencv 用新的3.2吧， 迟升级，早升级，迟早要升级， 不如用新的
https://github.com/opencv/opencv/archive/3.2.0.zip
 下载来下解压到一个目录， 例如c:\cv\下
把C:\CV\opencv\build\python\2.7 文件夹下所有文件， 也就两个文件， 复制到C:\CV\Python27\Lib\site-packages下， 安装基本完成
安装完成后， 做一个简单的脚本， 显示一张图片， 找张图片， 存为test.jpg, 下面的脚本存为test.py， 双击运行， 顺利的话， 应该能看到你的图片
import cv2
 img=cv2.imread('test.jpg')
 cv2.imshow('test',img)
 cv2.waitKey(0)
