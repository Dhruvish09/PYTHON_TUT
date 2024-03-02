"Multilevel Inheritance / Hierarchy Inheritance"

# Collage -> Department -> Student


class Collage:
    def __init__(self,collage_name,location):
        self.collage_name = collage_name
        self.location = location

    def get_collage_info(self):
        print(f"Collage name is {self.collage_name} and location is {self.location}")

class Department(Collage):
    def __init__(self,collage_name,location,department_name):
        super().__init__(collage_name,location)
        self.department_name = department_name

    def get_department_info(self):
        print(f"Department name is {self.department_name} in {self.collage_name}")

class Student(Department):
    def __init__(self,collage_name,location,department_name,student_name,age):
        super().__init__(collage_name,location,department_name)
        self.student_name = student_name
        self.age = age

    def get_student_info(self):
        super().get_collage_info()
        super().get_department_info()
        print(f"Name of Student is {self.student_name} and Age is {self.age}")

s1 = Student("SPECT","Anand","IT","Rahul",22)

s1.get_student_info()