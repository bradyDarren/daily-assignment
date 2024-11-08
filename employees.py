
class Employees:

    dp_categories = ["dp1","dp2"]

    def __init__(self, employee_list):
        self.employee_list = employee_list

    def retreive_name(self, emp_number):
        if emp_number in self.employee_list:
            return f"{self.employee_list[emp_number]["firstname"]} {self.employee_list[emp_number]["lastname"]}"
        else: 
            return (f"{emp_number} is not within the database.")
    
    def remove_assigned(self, emp_number):
        if emp_number in self.employee_list:
            del self.employee_list[emp_number]
        
    def check_user_input(self, user_emp_num):
        if user_emp_num in list(self.employee_list.keys()):
            return True
        else:
            return False

    def employee_level(self, partner):
        if self.employee_list[partner]["classification"] == 1:
            return True
        elif self.employee_list[partner]["classification"] == 2:
            return False

# class DP1(Employees):

#     def __init__(self, emp_num, f_name, l_name, level) -> None:
#         super().__init__(emp_num, f_name, l_name)
#         self.level = level
    
# class DP2(Employees):
#     def __init__(self, emp_num, f_name, l_name, level) -> None:
#         super().__init__(emp_num, f_name, l_name)
#         self.level = level


