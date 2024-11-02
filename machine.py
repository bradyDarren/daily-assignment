
class DP1Machines:

    machines = {
        "red": 2,
        "green": 2,
        "blue": 1,
        "orange": 4
    }

    def get_assignements_1(self):
        # prints a current report of all of the possible DP1 assignments
        one_options = ""
        for baler in self.machines:
            one_optionsoptions += f"{baler}/"
        return one_options
        

class DP2Machines:

    riding_machines = {
        "claw" : 1,
        "forklift" : 2
    }

    def get_assignment_2(self):
        two_options = ""
        for assignment in self.riding_machines:
            two_options += f"{assignment}/"
        return two_options
