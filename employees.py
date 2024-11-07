
class Employees:

    dp_categories = ["dp1","dp2"]

    def __init__(self, employee_list):
        self.employee_list = employee_list

    def retreive_name(self, emp_number):
        if emp_number in self.employee_list:
            print (f"{self.employee_list[emp_number]["firstname"]} {self.employee_list[emp_number]["lastname"]}")
        else: 
            print (f"{emp_number} is not within the database.")
    
    def remove_assigned(self, emp_list, emp_number):
        if emp_number in emp_list:
            del emp_list[emp_number]

    # def employee_level(self, emp_number, emp_list):


# class DP1(Employees):

#     def __init__(self, emp_num, f_name, l_name, level) -> None:
#         super().__init__(emp_num, f_name, l_name)
#         self.level = level
    
# class DP2(Employees):
#     def __init__(self, emp_num, f_name, l_name, level) -> None:
#         super().__init__(emp_num, f_name, l_name)
#         self.level = level


