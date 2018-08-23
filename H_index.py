from pymongo import MongoClient
from collections import Counter

# client = MongoClient('localhost',27017)
# db = client.runoob
# collection2 = db.scholarReal
# for personInfo in collection2.find().batch_size(10):
#     with open("./closeness_centrality.txt","a") as f:
#         f.write(str(personInfo["ID"])+"\n")

with open("./closeness_centrality.txt","r") as f:
    count = {}
    for i in f.readlines():
        if i not in count:
            count[i] = 0
            count[i] += 1
        else:
            count[i] += 1
    c = sorted(Counter(count).most_common(),key=lambda student: student[0],reverse=True)
with open("./frequency.txt","a") as f:
    f.write(str(c))
