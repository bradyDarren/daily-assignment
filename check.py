
class checks: 

    def check_int(self, prompt):
        while True: 
            try:
                return int(input(prompt))
            except ValueError: 
                print("Invalid input. Please ensure that you input a number next time.")

    