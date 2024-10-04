class Student:
    
    def __init__(self, name, registrationNo, program):
        self.name = name
        self.registrationNo = registrationNo
        self.program = program
        
        #display student details
    def display_student_details(self):
        print(f"Student name: {self.name} Registration No: {self.registrationNo} Program name: {self.program}")
        
        #allow input

name = input("Enter your name: ")
registrationNo = input("Enter resgitration number:")
program = input("Enter program: ")

#create object
student1 = Student(name, registrationNo, program)
        
student1.display_student_details()