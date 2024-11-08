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
    user_emp_num = input("Please enter your PeopleSoft Number: ").lower()

    if user_emp_num == "adj": 
        
    elif partner.check_user_input(user_emp_num):
        emp_level = partner.employee_level(user_emp_num)
        if emp_level:
            # generate a random selection when the user inputs there employee number. 
            rand_machine_1 = assignment_selection().assign_task(dp1_machines.machines)
            partner_name = partner.retreive_name(user_emp_num)
            removed_partner = partner.remove_assigned(user_emp_num)
            dp1_machines.adjust_demand_1(rand_machine_1)
            print(f"{partner_name} - {rand_machine_1}\n")
            dp1_machines.zero_demand(rand_machine_1)
        else:
            rand_machine_2 = assignment_selection().assign_task(dp2_machines.riding_machines)
            partner_name = partner.retreive_name(user_emp_num)
            removed_partner = partner.remove_assigned(user_emp_num)
            dp2_machines.adjust_demand_2(rand_machine_2)
            print(f"{partner_name} - {rand_machine_2}\n")
            dp2_machines.zero_demand(rand_machine_2)
    else: 
        print("PeopleSoft # not found. Please input a valid PeopleSoft #.")
    

