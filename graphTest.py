# -*- coding: utf-8 -*-
import sys
from pymongo import MongoClient
from igraph import *
from collections import Counter

reload(sys)
sys.setdefaultencoding('utf-8')

with open("./clustering_history.txt","r") as f:
    a = f.read()
    b = a.replace(")","\n")
    c = b.replace(","," ")
    d = c.replace("(","")
with open("./clustering_history_end.txt","a") as f:
    f.write(d)

# with open("./clustering_history.txt","r") as f:
#     a = f.read()
#     b = a.replace("),","\n")
# with open("./clustering_history_1.txt","r") as f:
#     a = f.read()
#     c = a.replace(",","")
# with open("./clustering_history_2.txt","a") as f:
#     f.write(c)

#出现频率计数
# with open("./clustering_1.txt","r") as f:
#     count = {}
#     for i in f.readlines():
#         a = i.split(" ")
#         b = float(a[2])
#         if b not in count:
#             count[b] = 0
#             count[b] += 1
#         else:
#             count[b] += 1
#     c = sorted(Counter(count).most_common(),key=lambda student: student[0],reverse=True)
# with open("./clustering_history.txt","a") as f:
#     f.write(str(c))







# with open("./connected_components.txt","r") as f:
#     a = f.read()
#     b = a.replace(",","\n")
# with open("./connected_components_1.txt","a") as f:
#     c = b.replace("'","")
#     f.write(c)


# g = Graph()
# nodes = []
# for i in range(1,50):
#     nodes.append(str(i))
# g.add_vertices(nodes)
# j = [('32','21'),('21','32')]
# g.add_edges(j)
# plot(g)
# print g
