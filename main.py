from data import employees_data
from employees import Employees, Classification
from machine import machines, riding_machines

people_f_name = []

for emp_data in employees_data:
    department = Employees(emp_num=emp_data["employee id"],
                           f_name=emp_data["first name"],
                           l_name=emp_data["last name"])
    people_f_name.append(department.f_name)
    print(people_f_name)