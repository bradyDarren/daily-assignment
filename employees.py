
class Employees:

    def retreive_name(self, emp_list, emp_number):
        if emp_number in emp_list:
            print (f"{emp_list[emp_number]["firstname"]} {emp_list[emp_number]["lastname"]}")
        else: 
            print (f"{emp_number} is not within the database.")
    
    def remove_assigned(self, emp_list, emp_number):
        if emp_number in emp_list:
            del emp_list[emp_number]

# class DP1(Employees):

#     def __init__(self, emp_num, f_name, l_name, level) -> None:
#         super().__init__(emp_num, f_name, l_name)
#         self.level = level
    
# class DP2(Employees):
#     def __init__(self, emp_num, f_name, l_name, level) -> None:
#         super().__init__(emp_num, f_name, l_name)
#         self.level = level


