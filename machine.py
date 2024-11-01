
class DP1Machines:

    machines = {
        "red": 2,
        "green": 2,
        "blue": 1,
        "orange": 4
    }

    def get_assignements_1(self):
        # prints a current report of all of the possible DP1 assignments
        options = ""
        for baler in self.machines:
            options += f"{baler}/"
        return options
        

class DP2Machines:
    riding_machines = {
        "claw" : 1,
        "forklift" : 2
    }

x = DP1Machines()

print(x.get_assignements_1()[:-1])
