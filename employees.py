
class Employees:
    def __init__(self, emp_num, f_name, l_name) -> None:
        self.emp_num = emp_num
        self.f_name = f_name
        self.l_name = l_name

class Classification(Employees):
    def __init__(self, emp_num, f_name, l_name, level) -> None:
        super().__init__(emp_num, f_name, l_name)
        self.level = level