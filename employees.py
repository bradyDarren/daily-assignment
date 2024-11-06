
class Employees:
    def __init__(self, emp_num, f_name, l_name) -> None:
        self.emp_num = emp_num
        self.f_name = f_name
        self.l_name = l_name
    
    def retreive_name(self, emp_number, employee_list):
        if emp_number in employee_list:
            return f"{employee_list[emp_number]["firstname"]} {employee_list[emp_number]["lastname"]}"
        else: 
            return f"{emp_number} is not within the database."

# class DP1(Employees):

#     def __init__(self, emp_num, f_name, l_name, level) -> None:
#         super().__init__(emp_num, f_name, l_name)
#         self.level = level
    
# class DP2(Employees):
#     def __init__(self, emp_num, f_name, l_name, level) -> None:
#         super().__init__(emp_num, f_name, l_name)
#         self.level = level
