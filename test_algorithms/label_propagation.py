import sys
import csv
from networkx.algorithms.community import asyn_lpa_communities

from functions import modularity
import read_network

def main(argv):

    g = read_network.read_static_network(argv[1])

    label_propagation_algorithm_output = list(asyn_lpa_communities(g))
    print('''modularité maximale détectée par l'algorithme de propagation d'étiquettes: ''', modularity(g, label_propagation_algorithm_output))

if __name__ == '__main__':
    sys.exit(main(sys.argv))