from data import employees_data
from employees import Employees
from machine import DP1Machines, DP2Machines
from check import checks
import random 

# list the types of assignments available for category one partners: 
dp1_assignments = DP1Machines().get_machine_1()[:-1]
print(dp1_assignments)

print()

# list the types of assignments available for category two partners: 
dp2_assignments = DP2Machines().get_machine_2()[:-1]
print(dp2_assignments)

print() 

# user_emp_num = checks().check_int("Please enter your PeopleSoft Number: ")


# random output from machines
# rand_machine = random.choice(list(DP1Machines().machines.keys()))
# print(rand_machine)