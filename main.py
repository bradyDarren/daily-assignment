from data import employees_data
from employees import Employees
from machine import DP1Machines, DP2Machines
from check import checks
import random 

# list the types of assignments available for category one partners: 
dp1_machines = DP1Machines()

# list the types of assignments available for category two partners: 
dp2_machines = DP2Machines()

# random output from machines
# rand_machine = random.choice(list(DP1Machines().machines.keys()))
# print(rand_machine)

while True:
    
    print(dp1_machines.message)
    print(dp1_machines.get_machine_1())
    print(dp2_machines. get_machine_2())

    user_emp_num = checks().check_int("Please enter your PeopleSoft Number: ")
