import networkx as nx

G = nx.Graph()
nodesList = []

for i in range(1,854873):
    nodesList.append(str(i))
nodesTuple = tuple(nodesList)
G.add_nodes_from(nodesTuple)

with open("./all_edge.txt","r") as f:
    edge = []
    for line in f.readlines():
        temp = line.split()
        edge.append((temp[0],temp[1]))
    G.add_edges_from(edge)

# close = nx.closeness_centrality(G)
# with open("./closeness_centrality.txt","a") as f:
#     f.write(str(close))

# avg_closeness =  sum(close.values())/len(close)
# with open("./avg_closeness_centrality.txt","a") as e:
#     e.write(str(avg_closeness))


with open("./degreeHistogram.txt","a") as f:
    result = nx.degree_histogram(G)
    f.write(str(result))





# plt.figure(figsize = (26, 26))
# pos = nx.spring_layout(G)
# nx.draw_networkx_labels(G, pos, font_color='k', font_size = 14)
# nx.draw(G, pos, node_size = 20, edge_color = 'grey', width = 0.4, arrows = True)
#
# plt.title("Justin Wolfers' Google Scholar Network", fontsize=40)
# plt.xticks([])
# plt.yticks([])
# plt.show()

# sub = nx.connected_component_subgraphs(G)[0]
# nx.diameter(sub)
# nx.average_shortest_path_length(sub)


# a = nx.connected_components(G)
# print max(nx.connected_components(G), key=len)
# print nx.average_clustering(G)
# print nx.clustering(G)
# print nx.average_shortest_path_length(G)






# for i in range(1,3198315):





