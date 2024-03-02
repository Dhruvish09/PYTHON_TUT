# Simple inheritance

# Student -> Collage

class Collage:
    def __init__(self,collage_name):
        self.collage_name = collage_name

    def get_collage_name(self):
        print(f"Collage name is {self.collage_name}")
    
class Student(Collage):
    def __init__(self, collage_name,student_name):
        super().__init__(collage_name)
        self.student_name = student_name

    def get_student_name(self):
        print(f"Student name is {self.student_name}")
    
std = Student("SPEC","Dhruvish")

std.get_student_name()
std.get_collage_name()


# Here, std is an instance of the Student class. 
# It is created from the Student class and has its own set of attributes (collage_name, location, department_name, student_name, and age)
# based on the parameters passed during its creation.
