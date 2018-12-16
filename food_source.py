class food_source(object):

    def __init__(self, initial_solution, initial_cost):
        
        super(food_source, self).__init__()

        self.trials = 0
        
        self.solution = initial_solution
        self.cost = initial_cost

    def increment_trials(self):
        self.trials +=1
    
    def __repr__(self):
        
        return f'<food_source s:{self.solution} f:{self.cost} />'