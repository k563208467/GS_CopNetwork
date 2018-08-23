# -*- coding: utf-8 -*-
import string
import networkx as nx

G = nx.Graph()
H = nx.Graph()
nodesList = []


# with open("./nanotechnology_nodes.txt","r") as f:
#     for i in f.readlines():
#         nodesList.append(i)
#
# nodesTuple = tuple(nodesList)
#
# print nodesTuple
# G.add_nodes_from(nodesTuple)
'''由边建立图'''
with open("./nanotechnology/nanotechnology_edges.txt","r") as f:
    edge = []
    for line in f.readlines():
        temp = line.split()
        edge.append((temp[0],temp[1]))
G.add_edges_from(edge)

'''度分布'''
# with open("./robotics_degreeHistogram.txt","a") as f:
#     result = nx.degree_histogram(G)
#     f.write(str(result))

'''子图分布'''
# with open("./robotics_connectednodes.txt  ","a") as f:
#     f.write(str(max(nx.connected_components(G), key=len)))

'''求得最大连通子图'''
# l = []
# ass = nx.connected_component_subgraphs(G, copy=True)
# for a in ass:
#     l.append(len(a.edges))
# l1 = sorted(l,reverse=True)
# asss = nx.connected_component_subgraphs(G, copy=True)
# for a in asss:
#     if len(a.edges) == l1[0]:
#         H.add_edges_from(a.edges)


'''最大连通子图直径(max)'''
# print  nx.diameter(H)

'''平均最短路径(max)'''
# print nx.average_shortest_path_length(H)

'''平均聚集系数(max)'''
# print nx.average_clustering(H)

'''聚集系数(max)'''
# with open("./robotics_clustering.txt","a") as f:
#     f.write(str(nx.clustering(H)))

'''度'''
# with open("./robotics_degree.txt","a") as f:
#     f.write(str(nx.degree(G)))

'''连通分支分布'''
# ls = []
# with open("./robotics_subgraph_size.txt","a") as f:
#     a = sorted(nx.connected_components(G),key=len,reverse=True)
#     for i in a:
#         ls.append(len(i))
#     f.write(str(ls))

'''K-core分布'''
# with open("./robotics_kcore.txt","a") as f:
#     G.remove_edges_from(nx.selfloop_edges(G))
#     f.write(str(nx.core_number(G)))

'''介数中心性'''
close = nx.closeness_centrality(G)
with open("./nanotechnology/nanotechnology_closeness_centrality.txt","a") as f:
    f.write(str(close))

