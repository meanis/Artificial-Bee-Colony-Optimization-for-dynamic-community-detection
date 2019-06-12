import sys
import csv
from networkx.algorithms.community import greedy_modularity_communities

from functions import cost
import read_network

def main(argv):

    g = read_network.read_static_network(argv[1])

    cnm_output = greedy_modularity_communities(g)
    print('modularité maximale détectée par CNM: ', cost(cnm_output, g))

if __name__ == '__main__':
    sys.exit(main(sys.argv))