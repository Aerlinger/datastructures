def dijkstra(G,v):
    dist_so_far = {}
    dist_so_far[v] = 0
    final_dist = {}
    while len(final_dist) < len(G):
        w = shortest_dist_node(dist_so_far)
        # lock it down!
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                elif final_dist[w] + G[w][x] < dist_so_far[x]:
                    dist_so_far[x] = final_dist[w] + G[w][x]
    return final_dist

def shortest_dist_node(distances):
    best_node = 'undefined'
    best_value = 1e9
    for v in distances:
        if distances[v] < best_value:
            (best_node, best_value) = (v, distances[v])

    return (best_node, best_value)

import random


def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

flights = [(1,2),(1,3),(2,3),(2,6),(2,4),(2,5),(3,6),(4,5)]
G = {}
for (x,y) in flights: make_link(G,x,y)

def clustering_coefficient(G,v):
    neighbors = G[v].keys()
    if len(neighbors) == 1: return 0.0
    links = 0.0
    for w in neighbors:
        for u in neighbors:
            if u in G[w]: links += 0.5
    return 2.0*links/(len(neighbors)*(len(neighbors)-1))


v = 2
print "CC:", clustering_coefficient(G,v)

vindex = {}
d = 0
for w in G[v].keys():
    vindex[d] = w
    d += 1

total = 0
for i in range(1,1000):
    if d > 1:
        pick = random.randint(0,d-1)
        v1 = vindex[pick]
        v2 = vindex[(pick+random.randint(1,d-1))%d]
        if v2 in G[v1]: total += 1
    print i, (total+0.0)/i