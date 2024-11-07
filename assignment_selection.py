import random

class assignment_selection: 

    def assign_task(self, assign_list):
        # generates a random assignment based on the given dict. 
        assignment = random.choice(list(assign_list.keys()))
        return assignment
