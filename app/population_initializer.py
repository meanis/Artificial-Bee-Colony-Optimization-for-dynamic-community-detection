import random as rand
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities

import functions as fun
from food_source import food_source

class population_initializer(object):
    
    def __init__(self, sigma, nb_s):
        super(population_initializer, self).__init__()

        ######################################################

        self.rand_fs_number = round(nb_s * (1 - sigma))
        self.elite_fs_number = round(nb_s * sigma)

        ######################################################

    def init_snapshot_pop(self, snapshot):

        self.snapshot = snapshot

        population = []

        rand_population = [self.random_selection() for _ in range(self.rand_fs_number)]
        population.extend(rand_population)

        elite_population = [self.elite_selection() for _ in range(self.elite_fs_number)]
        population.extend(elite_population)

        return population

    def random_selection(self):

        n = self.snapshot.number_of_nodes()

        solution = []

        for i in range(0, n):
            try:
                solution.append(rand.choice(list(self.snapshot[i])))
                #solution = [rand.choices(list(self.snapshot[i]), self.pearson_correlation[i])[0] for i in range(n)]
            except IndexError:
                solution.append(i)

        cost = self.cost(solution)

        return food_source(solution, cost)

    def elite_selection(self):

        solution = [ 0 for _ in range(0, self.snapshot.number_of_nodes()) ]

        for c in greedy_modularity_communities(self.snapshot):
            for node1 in c:
                for node2 in c:
                    if (node2 in self.snapshot[node1]):
                        solution[node1] = node2
        cost = self.cost(solution)

        return food_source(solution, cost)

    def cost(self, solution):

        community_structure = fun.locus_decode(solution)
        return fun.modularity(self.snapshot, community_structure)