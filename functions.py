from sklearn.metrics.cluster import normalized_mutual_info_score
from scipy.stats import pearsonr
import networkx as nx

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

    return normalized_mutual_info_score(A, B)

def pearson_correlation(snapshot):
    return None

def locus_decode(solution):

    n = len(solution)
    g = nx.Graph()
    
    for i in range(n):
        g.add_edge(i, solution[i])

    return list(nx.connected_components(g))