from scrapy import cmdline
cmdline.execute("scrapy crawl doubanmovie".split())

# -*- coding: utf-8 -*-
# import pymongo
#
# connection = pymongo.MongoClient()
# tdb = connection.Jikexueyuan
# post_info = tdb.test
# jike = {'name': u'123', 'age': '5', 'skill': 'python'}
# jike2 = {'name': u'1234', 'age': '5', 'skill': 'python'}
# xueyuan = {'name': u'12345', 'age': '50', 'skill': 'java', 'other': 'nothing'}
# post_info.insert(jike)
# post_info.insert(jike2)
# post_info.insert(xueyuan)
# post_info.remove({'age': '5'})