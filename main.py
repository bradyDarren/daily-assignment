from data import employees_data
from employees import Employees, DP1, DP2
from machine import DP1Machines, DP2Machines
from assignment_selection import assignment_selection

assignment = assignment_selection(employees_data)

print(assignment.retreive_name(emp_number="3955185"))

# people_f_name = []

# for emp_data in employees_data:
#     department = Employees(emp_num=emp_data["employee id"],
#                            f_name=emp_data["first name"],
#                            l_name=emp_data["last name"])
#     people_f_name.append(department.f_name)
#     print(people_f_name)