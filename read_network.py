from os import listdir
import re
import csv
from copy import deepcopy

import networkx as nx
from networkx.algorithms.community import LFR_benchmark_graph as lfr_benchmark

#########################################################################

def read_static_network(file_, delimiter_):
    
    snapshots = []
    groundtruth_communities = []

    with open(file_) as file:

        reader = csv.reader(file, delimiter=delimiter_)

        g = nx.Graph()

        for line in reader:
            g.add_edge(line[0], line[1])
        g = nx.convert_node_labels_to_integers(g)
        
        snapshots.append(g)

    return snapshots, groundtruth_communities

#########################################################################

def read_dynamic_network(folder_, delimiter_):

    snapshots = []
    groundtruth_communities = []
    
    network_files = [file_ for file_ in listdir(folder_) if re.match('^graph+.*.csv$', file_)]
    g = nx.Graph()
    
    for file_ in network_files:

        g.remove_edges_from(list(g.edges))
        
        file = open(folder_ + '/' + file_)
        
        reader = csv.reader(file, delimiter=delimiter_)

        for line in reader:
            g.add_edge(line[0], line[1])
        
        snapshots.append(deepcopy(g))

    snapshots = [nx.convert_node_labels_to_integers(g) for g in snapshots]
    
    return snapshots, groundtruth_communities

#########################################################################

def read_temporal_network(file_, delimiter_, snapshot_step, snapshot_overlap):

    snapshots = []
    groundtruth_communities = []
    
    return snapshots, groundtruth_communities

#########################################################################

def read_lfr_benchmark_network():

    snapshots = []
    groundtruth_communities = []

    n = 250
    tau1 = 3
    tau2 = 1.5
    mu = 0.1
    g = lfr_benchmark(n, tau1, tau2, mu, average_degree=5, min_community=20, seed=10)
    snapshots.append(g)

    #groundtruth_communities = {frozenset(g.nodes[v]['community']) for v in g}

    return snapshots, groundtruth_communities

#########################################################################