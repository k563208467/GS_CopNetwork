# -*- coding: utf-8 -*-
from pymongo import MongoClient
import time
import threading
from collections import Counter
client = MongoClient('localhost',27017)
db = client.runoob
collection = db.scholarReal
import string
#
# fieldLists = []
# for personInfo in collection.find().batch_size(10):
#     field = personInfo['Fields']
#     for i in field:
#         a = i.lower()
#         fieldLists.append(a)
#
# res = Counter(fieldLists)
#
# with open("./fields_frequency.txt","a") as f:
#     f.write(str(res))
#
# with open("./backgrounds_frequency.txt","r") as f:
#     a = f.read()
#     b = a.replace(",","\n")
#     c = b.replace(":"," ")
#     d = c.replace("u'","")
#     e = d.replace("'","")
#
#
# with open("./backgrounds_frequency_1.txt","a") as f:
#     f.write(str(e))
#
#
#  lists = []
# with open("./fields_frequency_2.txt","r") as f:
#     for i in f.readlines():
#         a = i.split(" ",2)
#         b = str(a[1]+"-"+a[2])
#         lists.append(b)
# with open("./fields_frequency_3.txt","a") as f:
#     f.write(str(lists))

# with open("./fields_frequency_4.txt","r") as f:
#     a = f.read()
#     b = a.replace("\\","")
#     # e = d.replace("\n","")
# with open("./fields_frequency_5.txt","a") as f:
#     f.write(b)


# with open("./Back_1.txt","r") as f:
#     for i in f.readlines():
#         a = i.split(" ",)
#         distance = len(a)
#         b = a[distance-1]
#         c = i.replace(b,"")
#         with open("./Back_no_1.txt","a") as e:
#             e.write(c+'\n')

a = "computer vision"
for personInfo in collection.find().batch_size(10):
    b = str(personInfo['Fields']).lower()
    if string.find(b,a) != -1:
        with open("./computer_vision_nodes.txt","a") as f:
            f.write(str(personInfo['orderNum'])+"\n")
        with open("./computer_vision_edges.txt","a") as g:
            if len(personInfo['Co_index']) == 0:
                    continue
            else:
                for i in personInfo['Co_index']:
                    g.write(str(personInfo["orderNum"])+" "+str(i)+'\n')







