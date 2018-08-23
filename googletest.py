from scholarNetwork import scholarNetwork
import matplotlib.pyplot as plt
import networkx as nx

scholar = 'https://scholar.google.com/citations?user=MXgWgmEAAAAJ&hl=en&oi=ASCII'
nodes = 52
g = scholarNetwork.getGraph(scholar, nodes)

plt.figure(figsize = (40, 40))
pos = nx.spring_layout(g)
nx.draw_networkx_labels(g, pos, font_color='k', font_size = 12)
nx.draw(g, pos, node_size = 20, edge_color = 'grey', width = 0.4, arrows = True)

plt.title("Zhou Tao's Google Scholar Network", fontsize=40)
plt.xticks([])
plt.yticks([])
plt.show()

