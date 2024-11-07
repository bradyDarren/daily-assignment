
class DP1Machines:

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
            baler += (f"{count}. {machine_name} tasks remaining : {self.machines[machine_name]}\n")
        return baler
    
    def get_demand_1(self):
        total_demand_1 = 0
        for value in self.machines:
            total_demand_1 += self.machines[value]
        return total_demand_1

    def adjust_demand_1(self, machine):
        if machine in self.machines:
            demand = self.machines[machine]
            if demand > 0:
                self.machines[machine] = demand - 1

class DP2Machines:

    riding_machines = {
        "CLAW" : 1,
        "FORKLIFT" : 2
    }

    def get_machine_2(self):
        assignments = ''
        count = 0
        for task in self.riding_machines:
            count += 1
            assignments += (f"{count}. {task} tasks remaining : {self.riding_machines[task]}\n")
        return assignments
    
    def get_demand_2(self):
        total_demand_2 = 0
        for value in self.riding_machines:
            total_demand_2 += self.riding_machines[value]
        return total_demand_2 

    def adjust_demand_2(self, machine):
        if machine in self.riding_machines:
            demand = self.riding_machines[machine]
            if demand > 0: 
                self.riding_machines[machine] = demand - 1


# test lines

# x = DP1Machines()
# print(x.get_machine_1())
# print(DP1Machines().get_demand_1())
# print(DP2Machines().get_demand_2())
# print(DP2Machines().get_machine_2())
# x.adjust_demand_1("RED")
# print(x.machines)