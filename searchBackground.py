# -*- coding: utf-8 -*-
from pymongo import MongoClient
import time
import threading
from collections import Counter
import string
client = MongoClient('localhost',27017)
db = client.runoob
collection = db.scholarReal
#
# fieldLists = []
# for personInfo in collection.find().batch_size(10):
#     field = personInfo['Affi']
#     for i in field:
#         a = i.lower()
#         fieldLists.append(a)
#
# res = Counter(fieldLists)
# with open("./backgrounds_frequency.txt","a") as f:
#     f.write(str(res))

# with open("./backgrounds_frequency_special.txt","r") as f:
#     a = f.read()
#     b = a.replace("","")
#
# with open("./backgrounds_frequency_2.txt","a") as f:
#     f.write(b)
#
# with open("./Back_list.txt","a") as f:
#      for personInfo in collection.find().batch_size(10):
#          f.write(str(personInfo['Affi']) + "@@@" +str(personInfo['orderNum'])+"&&&" +str(personInfo['Co_index']) + '\n')
#
# with open("./Back_no_1.txt","r") as f:
#     for i in f.readlines():
#         j = i.strip()
#         print j
#         for personInfo in collection.find().batch_size(10):
#             # if j in str(personInfo['Affi']):
#             b = str(personInfo['Affi']).lower()
#             if string.find(b,j) != -1:
#                 print personInfo['orderNum']
#                 back = j
#                 # cos = personInfo['Co_index']
#                 # for co in cos:
#                 collection.update({"orderNum":personInfo['orderNum']},{'$set':{"University_college":back}})
#                 # collection.update({"orderNum":personInfo['orderNum']},{'$set':{"Company_organization":back}})
#                 # id = personInfo['orderNum']
#                 # co_relationship = personInfo['Co_index']

# for personInfo in collection.find().batch_size(10):
#     if collection.find({"University_college":{"$exists":True}}):
#         print 1
'''洗边'''
def dataset(start,stop):
    for personInfo in collection.find({"orderNum":{ '$gt':start,'$lt':stop}}).batch_size(10):
        print personInfo['orderNum']
        if len(personInfo['Coauthor']) == 0:
            list = []
            collection.update(personInfo,{'$set':{"CoCompany_index":list}})
        else:
            list = []
            for person in personInfo['Coauthor']:

                personId = collection.find_one({"Name": person})
                if personId is not None:
                    if personId.has_key('Company_organization') is True:
                        list.append(personId["Company_organization"])

            collection.update(personInfo,{'$set':{"CoCompany_index":list}})
t1 = threading.Thread(target=dataset,args=(85292,200000))
t1.start()
t2 = threading.Thread(target=dataset,args=(257509,400000))
t2.start()
t3 = threading.Thread(target=dataset,args=(461696,600000))
t3.start()






