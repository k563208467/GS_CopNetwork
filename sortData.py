# -*- coding: utf-8 -*-
import sys
from pymongo import MongoClient
from igraph import *

reload(sys)
sys.setdefaultencoding('utf-8')

client = MongoClient('localhost',27017)
db = client.runoob
collection = db.scholarData

count_scholar = 0
count_cooperrations = 0
scholar_name = []
coo_scholar_name = []
g = Graph()
nodes = []
personList = []

#建节点
for i in range(1,3198314):
    nodes.append(str(i))
g.add_vertices(nodes)

#建边
with open("./edge.txt","r") as f:
    edge = []
    for line in f.readlines():
        temp = line.split()
        edge.append((temp[0],temp[1]))
    g.add_edges(edge)

# print g.community_label_propagation()
print g.pagerank()
# print g.induced_subgraph()

# g.subcomponent()






# if __name__ == '__main__':
#     print("Creating the full newworks")
#     client = MongoClient('localhost',27017)
#     db = client.runoob
#     collection = db.scholarData
#
#     count_scholar = 0
#     count_cooperrations = 0
#     scholar_name = []
#     coo_scholar_name = []
#     g = Graph()
#     list = []
#     personList = []
#
#
# ***************************************************
# f = open('yourtest.txt','r')
# test = {}
# for i in f.readlines()[1:]:
#     people,friends = i.split()[0],i.split()[1:] //根据自己数据集去索引相应内容
#     test.setdefault(people,friends)
#
# g = Graph()
# for i in test.keys():
#     g.add_vertices(str(i))
# edges = []
# for i in test.keys():
#     for j in test[i]:
#         edges.append((str(i),str(j)))

# 去重
# new = []
# for i in edges:
#     new.append(tuple(sorted(list(i))))
#
# g.add_edges(set(new))
