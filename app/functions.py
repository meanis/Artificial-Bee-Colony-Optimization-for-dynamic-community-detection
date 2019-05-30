from sklearn.metrics.cluster import normalized_mutual_info_score
from scipy.stats import pearsonr
import networkx as nx
import math

def modularity(snapshot, community_structure):

    m = snapshot.number_of_edges()

    e = []
    a = []

    for c in community_structure:

        i = snapshot.subgraph(c).number_of_edges()
        e.append(i/m)

        j = 0.0
        for n in c:
            j += snapshot.degree[n]
        a.append(j/(2*m))

    q = 0.0
    for ei,ai in zip(e,a):
        q += (ei - ai**2)

    return q

def NMI(A, B):
    A = node_labeling(A)
    B = node_labeling(B)
    return normalized_mutual_info_score(A, B)

def pearson_correlation(snapshot):

    r = []
    A = nx.to_numpy_array(snapshot)
    for n in range(snapshot.number_of_nodes()):
        l = []
        for m in snapshot[n]:
            x = pearsonr(A[n], A[m])[0]
            l.append(1 / (1 + math.exp(-x)))
        r.append(l)
    return r

def locus_decode(solution):

    n = len(solution)
    g = nx.Graph()

    for i in range(n):
        g.add_edge(i, solution[i])

    return list(nx.connected_components(g))

def node_labeling(solution):

    labels = [0 for _ in range(len(solution))]
    partition = locus_decode(solution)

    label = 0
    for community in partition:
        for member in community:
            labels[member] = label
        label += 1

    return labels