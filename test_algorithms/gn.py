import sys
import csv
from networkx.algorithms.community import girvan_newman

from functions import modularity
import read_network

def main(argv):

    g = read_network.read_static_network(argv[1])

    gn_output = list(girvan_newman(g))
    solutions = []
    for solution in gn_output:
        solutions.append(modularity(g, solution))
    
    print('modularité maximale détectée par Girvan et Newman: ', max(solutions))

if __name__ == '__main__':
    sys.exit(main(sys.argv))