##################################################################
# Traversal...
# Call this routine on nodes being visited for the first time
def mark_component(G, node, marked):
    marked.append(G[node])
    total_marked = 1
    for neighbor in G[node]:
        if neighbor not in marked:
            total_marked += mark_component(G, neighbor, marked)
    return total_marked

def check_connection(G, v1, v2):
    marked = {}
    mark_component(G, v1, marked)
    return v2 in marked

def list_component_sizes(G):
    marked = []
    for node in G.keys():
        if node not in marked:
            print "Component containing", node, ": ", mark_component(G, node, marked)

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def runhere():
    edges = [('a', 'g'), ('a', 'd'), ('g', 'c'), ('g', 'd'),
             ('b', 'f'), ('f', 'e'), ('e', 'h')]
    G = {}
    for v1, v2 in edges:
        make_link(G, v1, v2)
    list_component_sizes(G)

    assert check_connection(G, "a", "c") == True
    assert check_connection(G, 'a', 'b') == False

runhere()