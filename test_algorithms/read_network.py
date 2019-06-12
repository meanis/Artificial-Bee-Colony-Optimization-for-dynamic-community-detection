import csv

import networkx as nx

#########################################################################

def read_static_network(file_):

    with open(file_) as file:

        reader = csv.reader(file, delimiter=' ')

        g = nx.Graph()

        for line in reader:
            g.add_edge(line[0], line[1])
        g = nx.convert_node_labels_to_integers(g)

        print(nx.info(g)) # debug

    return g

#########################################################################