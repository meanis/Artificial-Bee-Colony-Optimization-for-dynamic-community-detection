import networkx as nx

def cost(cnm_output, network):

    solution = [ 0 for _ in range(0, network.number_of_nodes()) ]

    for c in cnm_output:
        for node1 in c:
            for node2 in c:
                if (node2 in network[node1]):
                    solution[node1] = node2
    
    community_structure = locus_decode(solution)
    q = modularity(network, community_structure)
    return q

def locus_decode(solution):

    n = len(solution)
    g = nx.Graph()

    for i in range(n):
        g.add_edge(i, solution[i])

    return list(nx.connected_components(g))

def modularity(network, community_structure):

    m = network.number_of_edges()

    e = []
    a = []

    for c in community_structure:

        i = network.subgraph(c).number_of_edges()
        e.append(i/m)

        j = 0.0
        for n in c:
            j += network.degree[n]
        a.append(j/(2*m))

    q = 0.0
    for ei,ai in zip(e,a):
        q += (ei - ai**2)

    return q