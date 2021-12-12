from igraph import *

FILE = 'distancies.txt'

g = Graph.Read_Adjacency(FILE)
g.to_undirected()
plot(g, vertex_size=1, layout='circle', target='graph.png')

print('Computing fastgreedy:', end=' ')
c_fg = g.community_fastgreedy().as_clustering()
print('modularity: ', c_fg.modularity)
plot(c_fg, target='community_fastgreedy.png')

print('Computing infomap:', end=' ')
c_im = g.community_infomap()
print('modularity: ', c_im.modularity)
plot(c_im, target='community_infomap.png')

print('Computing leading eigenvector:', end=' ')
c_le = g.community_leading_eigenvector()
print('modularity: ', c_le.modularity)
plot(c_le, target='community_leading_eigenvector.png')

print('Computing label propagation:', end=' ')
c_lp = g.community_label_propagation()
print('modularity: ', c_lp.modularity)
plot(c_lp, target='community_label_propagation.png')

print('Computing multilevel:', end=' ')
c_ml = g.community_multilevel()
print('modularity: ', c_ml.modularity)
plot(c_ml, target='community_multilevel.png')

# print('Computing optimal modularity:', end=' ')
# c_om = g.community_optimal_modularity()
# print('modularity: ', c_om.modularity)
# plot(c_om, target='community_optimal_modularity.png')

# print('Computing edge betweenness:', end=' ')
# c_eb = g.community_edge_betweenness().as_clustering()
# print('modularity: ', c_eb.modularity)
# plot(c_eb, target='community_edge_betweenness.png')

# print('Computing spinglass:', end=' ')
# c_sl = g.community_spinglass()
# print('modularity: ', c_sl.modularity)
# plot(c_sl, target='community_spinglass.png')

# print('Computing walktrap:', end=' ')
# c_wt = g.community_walktrap().as_clustering()
# print('modularity: ', c_wt.modularity)
# plot(c_wt, target='community_walktrap.png')

print('Computing leiden:', end=' ')
c_l = g.community_leiden()
print('modularity: ', c_l.modularity)
plot(c_l, target='community_leiden.png')
