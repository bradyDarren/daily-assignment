
class DP1Machines:

    machines = {
        "red": 2,
        "green": 2,
        "blue": 1,
        "orange": 4
    }

    def get_machine_1(self):
        # prints a current report of all of the possible DP1 assignments
        baler = []
        count = 0
        for machine_name in self.machines:
            count += 1
            baler.append(f"{count}. {machine_name} remaining : {self.machines[machine_name]}")
        return baler
    

class DP2Machines:

    riding_machines = {
        "claw" : 1,
        "forklift" : 2
    }

    def get_machine_2(self):
        assignments = []
        count = 0
        for task in self.riding_machines:
            count += 1
            assignments.append(f"{count}. {task} remaining : {self.riding_machines[task]}")
        return assignments

x = DP1Machines()
print(x.get_machine_1())