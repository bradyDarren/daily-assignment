from data import employees_data
from employees import Employees, DP1, DP2
from machine import DP1Machines, DP2Machines
from assignment_selection import assignment_selection
from check import checks

employees_database = []

for employee in employees_data:
    if employees_data[employee]["classification"] == 1:
        e_database = Employees(employee, employees_data[employee]["firstname"], employees_data[employee]["lastname"])
        employees_database.append(e_database)

# test
# print(employees_database[0].emp_num)

# user_input = checks().check_int("Hello, Please input your Peoplesoft number : ")


# greeting = assignment_selection()