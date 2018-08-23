from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.runoob
collection = db.scholarReal
i = 1
# for personInfo in collection.find({"orderNum":{ '$gt':78691}}).batch_size(10):
# for personInfo in collection.find().batch_size(10):
#     collection.update(personInfo,{'$set':{"orderNum":i}},multi=True)
#     i = i+1
#     print i

for personInfo in collection.find({"orderNum":{ '$gt':854872}}).batch_size(10):
    with open("./all_edge.txt","a") as f:
        if len(personInfo['Co_index']) == 0:
           continue
        else:
            for i in personInfo['Co_index']:
                f.write(str(personInfo["orderNum"])+" "+str(i)+'\n')
        print personInfo['orderNum']






