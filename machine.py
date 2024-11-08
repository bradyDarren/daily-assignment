
class DP1Machines:

    message_1 = "Below is the DP1 assignments needed to be filled for the days tasks: \n"

    machines = {
        "RED": 2,
        "GREEN": 2,
        "BLUE": 1,
        "ORANGE": 4
    }

    def get_machine_1(self):
        # prints a current report of all of the possible DP1 assignments
        baler = ''
        count = 0
        for machine_name in self.machines:
            count += 1
            baler += (f"    {count}. {machine_name} tasks remaining : {self.machines[machine_name]}\n")
        return baler
    
    def get_demand_1(self):
        # returns the total amount of people needed wihtin the DP1 category.
        total_demand_1 = 0
        for value in self.machines:
            total_demand_1 += self.machines[value]
        return total_demand_1

    def adjust_demand_1(self, machine):
        if machine in self.machines:
            demand = self.machines[machine]
            if demand > 0:
                self.machines[machine] = demand - 1
    
    def zero_demand(self, machine_chosen_1):
        if self.machines[machine_chosen_1] == 0:
            del self.machines[machine_chosen_1]

class DP2Machines:

    message_2 = "Below is the DP2 assignments needed to be filled for the days tasks: \n" 

    riding_machines = {
        "CLAW" : 1,
        "FORKLIFT" : 2
    }

    def get_machine_2(self):
        # prints a current report of all of the possible DP2 assignments
        assignments = ''
        count = 0
        for task in self.riding_machines:
            count += 1
            assignments += (f"    {count}. {task} tasks remaining : {self.riding_machines[task]}\n")
        return assignments
    
    def get_demand_2(self):
        # returns the total amount of people needed wihtin the DP2 category.
        total_demand_2 = 0
        for value in self.riding_machines:
            total_demand_2 += self.riding_machines[value]
        return total_demand_2 

    def adjust_demand_2(self, machine):
        # reduces demand by 1 if task is assigned to an employee and above 0.
        if machine in self.riding_machines:
            demand = self.riding_machines[machine]
            if demand > 0: 
                self.riding_machines[machine] = demand - 1
    
    def zero_demand(self, machine_chosen_2):
        # removes the assignment from the list if the demand for the assignment is 0.
        if self.riding_machines[machine_chosen_2] == 0:
            del self.riding_machines[machine_chosen_2]


# test lines

x = DP1Machines()
# print(x.get_machine_1())
# print(DP1Machines().get_demand_1())
# print(DP2Machines().get_demand_2())
# print(DP2Machines().get_machine_2())
# x.adjust_demand_1("RED")
# print(x.machines)
# x.zero_demand("RED")
# print(x.machines)