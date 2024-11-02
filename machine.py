
class DP1Machines:

    machines = {
        "red": 2,
        "green": 2,
        "blue": 1,
        "orange": 4
    }

    def get_assignements_1(self):
        # prints a current report of all of the possible DP1 assignments
        baler = []
        for machine_name in self.machines:
            baler.append(machine_name)
        return baler
    

class DP2Machines:

    riding_machines = {
        "claw" : 1,
        "forklift" : 2
    }

    def get_assignments_2(self):
        assignments = []
        for task in self.riding_machines:
            assignments.append(task)
        return assignments
    