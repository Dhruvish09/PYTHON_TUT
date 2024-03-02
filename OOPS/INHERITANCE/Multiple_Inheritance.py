# Multiple Inheritance

# Student ->  Collage  + Department


class Collage:
    def __init__(self, collage_name, location):
        self.collage_name = collage_name
        self.location = location

    def get_collage_info(self):
        print(f"Collage name is {self.collage_name} and location is {self.location}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name

    def get_department_info(self):
        print(f"Department name is {self.department_name}")


class Student(Collage, Department):
    def __init__(self, collage_name, location, department_name, student_name, age):
        Collage.__init__(self, collage_name, location)
        Department.__init__(self, department_name)
        self.student_name = student_name
        self.age = age

    def get_student_info(self):
        super().get_collage_info() # call function from class Collage
        super().get_department_info() # call function from class Department
        print(f"Student name is {self.student_name} and age is {self.age}")


std = Student("SPEC", "Anand", "IT", "Dhruvish Patel", 21)

# std.get_collage_info() # call function from class Collage manually  if not call inside of instace class
# std.get_department_info() # call function from class Department manually if not call  inside of instace class
std.get_student_info()

