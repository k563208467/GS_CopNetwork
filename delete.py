from pymongo import MongoClient

# client = MongoClient('localhost',27017)
# db = client.runoob
# collection = db.scholarData
# collection2 = db.scholarReal
# for personInfo in collection2.find().batch_size(10):

#
# with open("./computer_vision_edges.txt","r") as f:
#     for i in f.readlines():
#         li = i.split()
#         with open("./computer_vision_nodes.txt","r") as g:
#             for j in g.readlines():
#                 if int(j) == int(li[1]):
#                     with open("./computer_vision_edges_1.txt","a") as h:
#                         h.write(str(i))
#                 else:
#                     continue
# l = []
# with open("./nanotechnology_edges.txt","r") as f:
#     for i in f.readlines():
#         li = i.split()
#         l.append(li[0])
#         l.append(li[1])
#
# m = list(set(l))
# print len(m)


with open("./artificial_intelligence/artificial_intelligence_subgraph_size.txt","r") as f:
    a = f.read()
    b = a.replace(",","\n")

with open("./artificial_intelligence/artificial_intelligence_subgraph_size_1.txt","a") as g:
    g.write(b)
