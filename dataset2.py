#!/usr/bin/python
# -*- coding:utf8 -*-
from pymongo import MongoClient
import time
import threading
from bson import json_util as jsonb


client = MongoClient('localhost',27017)
db = client.runoob
collection = db.scholarData

#通过nx的最大子图节点，在edge文件抽最大连通子图，有重复
def dataset():
    with open("./connected_components_1.txt","r") as f:
        for line in f.readlines():
            a = line.strip()
            b = collection.find({},{"orderNum":a})
            print b

            # with open("./max_component.txt","a") as h:


        # for personInfo in collection.find({"orderNum":{ '$lt':290001}}):
        #     if len(personInfo['Co_index']) == 0:
        #         continue
        #     else:
        #         for i in personInfo['Co_index']:
        #             f.write(str(personInfo["orderNum"])+" "+str(i)+'\n')
        #     print personInfo['orderNum']

dataset()
