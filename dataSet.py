from pymongo import MongoClient
import time
import threading

client = MongoClient('localhost',27017)
db = client.runoob
collection = db.scholarReal

def dataset(start,stop):
    for personInfo in collection.find({"orderNum":{ '$gt':start,'$lt':stop}}).batch_size(10):
        if len(personInfo['Coauthor']) == 0:
            list = []
            collection.update(personInfo,{'$set':{"Co_index":list}})
        else:
            list = []
            for person in personInfo['Coauthor']:

                personId = collection.find_one({"Name": person},["orderNum"])
                if personId is None:
                    print personInfo["orderNum"]

                else:
                    list.append(personId["orderNum"])
            collection.update(personInfo,{'$set':{"Co_index":list}})


t1 = threading.Thread(target=dataset,args=(854860,854874))
t1.start()
# t2 = threading.Thread(target=dataset,args=(679995,680005))
# t2.start()
# t3 = threading.Thread(target=dataset,args=(759995,760005))
# t3.start()




