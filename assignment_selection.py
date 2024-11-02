
class assignment_selection: 

    def __init__(self, employement_list) -> None:
        self.employement_list = employement_list
        self.dp1_count = 0
        self.dp2_count = 0
    
    def retreive_name(self, emp_number):
        if emp_number in self.employement_list:
            return self.employement_list[emp_number]["firstname"],self.employement_list[emp_number]["lastname"]
        else: 
            return f"{emp_number} is not within the database."

