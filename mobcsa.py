from operator import attrgetter
import copy
import random as rand
import numpy as np
import networkx as nx

from food_source import food_source
import functions as fun

class mobcsa(object):
    def __init__(self, params):
        super(mobcsa, self).__init__()
        
        ######################################################
        
        self.nb_s = int(params['nb_s'])
        self.nb_cycles = int(params['nb_cycles'])
        self.limit_cycles = int(params['limit_cycles'])
        self.employed_bees_number = self.nb_s
        
        E = params['employed_bees_percentage']
        self.onlooker_bees_number = round(self.nb_s * ((1 / E) - 1))

        ######################################################

        self.T0 = params['T0']
        self.Tmin = params['Tmin']
        self.alpha = params['alpha']
        self.cycles_per_t = int(params['cycles_per_t'])

        ######################################################

        self.gamma = params['gamma']
        self.delta = params['delta']

        ######################################################

        self.population = []
        self.initial_population = []

        ######################################################

        self.snapshot_analysis_data = {
            'global_optimal': []
        }
    
#########################################################################################
    
    def execute(self, snapshot, initial_population):
        
        self.snapshot_analysis_data = {
            'global_optimal': []
        }
        
        self.snapshot = snapshot
        self.pearson_correlation = fun.pearson_correlation(self.snapshot)
        
        self.population = self.repair_population(initial_population, self.snapshot)
        self.initial_population = copy.deepcopy(self.best_fs())
        self.global_best_fs = copy.deepcopy(self.best_fs())
        
        for _ in range(self.nb_cycles):
            self.employed_bees_stage()
            self.onlooker_bees_stage()
            self.scout_bees_stage()
            #self.simulated_annealing_stage(self.best_fs())
            
            if (self.best_fs().cost > self.global_best_fs.cost ):
                self.global_best_fs = copy.deepcopy(self.best_fs())
                print(self.global_best_fs.cost)  #debug

            self.snapshot_analysis_data['global_optimal'].append(self.global_best_fs.cost)

        return self.global_best_fs, self.population, self.snapshot_analysis_data

#########################################################################################

    def employed_bees_stage(self):
        
        for index in range(self.employed_bees_number):
            fs = self.population[index]
            new_fs = self.generate_fs(fs)

            best_fs = self.greedy_selection(fs, new_fs)

            self.update_fs(fs, best_fs)

#########################################################################################

    def onlooker_bees_stage(self):
        
        for _ in range(self.onlooker_bees_number):

            selected_fs = self.global_selection()
            new_fs = self.generate_fs(selected_fs)

            best_fs = self.greedy_selection(selected_fs, new_fs)
            self.update_fs(selected_fs, best_fs)

#########################################################################################

    def scout_bees_stage(self):
        
        for fs in self.population:

            if fs.trials > self.limit_cycles:
                
                new_fs = self.random_selection()
                
                fs.solution = new_fs.solution
                fs.cost = new_fs.cost
                fs.trials = new_fs.trials

#########################################################################################

    def accept(self, new_fs_cost, current_fs_cost, T):
        
        if (new_fs_cost > current_fs_cost):
            return True
        else:
            r = rand.uniform(1, np.e)
            return (r < ( np.exp( ( current_fs_cost - new_fs_cost ) / T ) ))
        
    def simulated_annealing_stage(self, fs):

        T = self.T0

        while T > self.Tmin:
            
            for _ in range(self.cycles_per_t):
                
                new_fs = self.generate_fs(fs)
                
                if self.accept(new_fs.cost, fs.cost, T):

                    fs.solution = new_fs.solution
                    fs.cost = new_fs.cost

            T = T * self.alpha

#########################################################################################

    def generate_fs(self, fs):

        new_solution = fs.solution.copy()

        n = len(fs.solution)
        indexes = range(0, n)
        chosen_indexes = rand.sample(indexes, int(n * self.delta))

        for i in chosen_indexes:
            try:
                #new_solution[i] = rand.choice(list(self.snapshot[i]))
                new_solution[i] = rand.choices(list(self.snapshot[i]), self.pearson_correlation[i])[0]
            except IndexError:
                new_solution[i] = i
            

        return food_source(new_solution, self.cost(new_solution))

#########################################################################################

    def greedy_selection(self, fs1, fs2):

        if fs1.cost > fs2.cost:
            return fs1
        else:
            return fs2

#########################################################################################

    def global_selection(self):
        
        sum_costs = sum([fs.cost for fs in self.population])
        probabilities = [(fs.cost / sum_costs) for fs in self.population]
        
        selected_fs = rand.choices(self.population, probabilities)[0]
        
        return selected_fs

#########################################################################################

    def random_selection(self):
        
        n = self.snapshot.number_of_nodes()
        
        solution = []

        for i in range(0, n):
            try:
                #solution.append(rand.choice(list(self.snapshot[i])))
                solution.append(rand.choices(list(self.snapshot[i]), self.pearson_correlation[i])[0])
            except IndexError:
                solution.append(i)
        
        
        
        cost = self.cost(solution)

        return food_source(solution, cost)

#########################################################################################

    def cost(self, solution):
        
        community_structure = fun.locus_decode(solution)
        cost = (self.gamma * fun.modularity(self.snapshot, community_structure)) + ((1-self.gamma) * fun.NMI(community_structure, community_structure))
        return cost

#########################################################################################

    def update_fs(self, fs, new_fs):
        
        if fs.cost == new_fs.cost:
            fs.increment_trials()
        else:
            fs.solution = new_fs.solution
            fs.cost = new_fs.cost
            fs.trials = new_fs.trials

#########################################################################################
    
    def best_fs(self):

        best_fs = max(self.population, key = attrgetter('cost'))
        return best_fs

#########################################################################################

    def repair_population(self, initial_population, snapshot):
        
        for fs in initial_population:
            
            for v in range(len(fs.solution)):
                
                if fs.solution[v] not in snapshot[v]:
                    try:
                        fs.solution[v] = rand.choice(list(self.snapshot[v]))
                    except IndexError:
                        fs.solution[v] = v
            
            for v in range(len(fs.solution), snapshot.number_of_nodes()):
                
                try:
                    fs.solution.append(rand.choice(list(self.snapshot[v])))
                except IndexError:
                    fs.solution.append(v)


            fs.cost = self.cost(fs.solution)

        return initial_population

#########################################################################################