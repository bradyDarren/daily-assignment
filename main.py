from data import employees_data
from employees import Employees
from machine import DP1Machines, DP2Machines
from check import checks
from assignment_selection import assignment_selection

# instances of classes
dp1_machines = DP1Machines()
dp2_machines = DP2Machines()
partner = Employees(employees_data)

while True:
    
    # printing out a report of the remaining assignments needing to be filled for both
    # DP1 and DP2. 
    print(dp1_machines.message_1)
    print(dp1_machines.get_machine_1())
    print(dp2_machines.message_2)
    print(dp2_machines. get_machine_2())

    # accepting user input
    user_emp_num = checks().check_int("Please enter your PeopleSoft Number: ")

    if partner.check_user_input(user_emp_num):
        # generate a random selection when the user inputs there employee number. 
        rand_machine = assignment_selection().assign_task(dp1_machines.machines)
        partner_name = partner.retreive_name(user_emp_num)
        removed_partner = partner.remove_assigned(user_emp_num)
        dp1_machines.adjust_demand_1(rand_machine)
        print(f"{partner_name} - {rand_machine}")
        print(dp1_machines.machines)
        print(employees_data)
    else: 
        print("PeopleSoft # not found. Please input a valid PeopleSoft #.")
    break

