# scrapytest
Python爬虫学习


MongoDB软件下载
http://pan.baidu.com/s/1sjZ9lxV
Scrapy安装
http://pan.baidu.com/s/1mhhQTxm


demo:https://github.com/gnemoug/distribute_crawler


环境：Windows7 python2.7.10（64位）
安装：easy_install scrapy

升级pip：pip install --upgrade pip

新建项目 (Project)：新建一个新的爬虫项目
明确目标（Items）：明确你想要抓取的目标
制作爬虫（Spider）：制作爬虫开始爬取网页
存储内容（Pipeline）：设计管道存储爬取内容

新建项目：
cmd>scrapy startproject tutorial
	scrapy.cfg：项目的配置文件
	tutorial/：项目的Python模块，将会从这里引用代码
	tutorial/items.py：项目的items文件
	tutorial/pipelines.py：项目的pipelines文件
	tutorial/settings.py：项目的设置文件
	tutorial/spiders/：存储爬虫的目录

明确目标

cmd>scrapy crawl dmoz
运行报错：
python：exceptions.ImportError: No module named win32api
解决：参考scrapy_install.pdf：http://www.feedbackward.com/content/scrapy_install.pdf

解决之后运行成功

xpath学习
w3school：http://www.w3school.com.cn/xpath/index.asp

官方文档：http://doc.scrapy.org/en/latest/intro/install.html#intro-install-platform-notes
参考：http://blog.csdn.net/pleasecallmewhy/article/details/19642329


Scrapy应用MongoDB

在settings.py中配置MongoDB的IP地址、端口、数据记录名称，可以实现方便的更换MongoDB的数据库信息。
在settings.py中引用pipelines.py从而使pipelines生效。

在pipelines中可以使用像普通Python文件操作MongDB一样编写代码处理需要保存到MongoDB的数据。
然而不同的是这里的数据来自items。这样做的好处是将数据的抓取和处理分开。


