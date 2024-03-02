#Hybrid Inheritance

# Base class representing a Collage
class Collage:
    def __init__(self, collage_name, location):
        self.collage_name = collage_name
        self.location = location

    def get_collage_info(self):
        print(f"Collage name is {self.collage_name} and location is {self.location}")


# Base class representing a Department
class Department:
    def __init__(self, department_name):
        self.department_name = department_name

    def get_department_info(self):
        print(f"Department name is {self.department_name}")


# Base class representing a University
class University:
    def __init__(self, university_name):
        self.university_name = university_name

    def get_university_info(self):
        print(f"University name is {self.university_name}")


# Derived class representing a Student
class Student(Collage, Department):
    def __init__(self, collage_name, location, department_name, student_name, age):
        # Multiple Inheritance: Student inherits from Collage and Department
        Collage.__init__(self, collage_name, location)
        Department.__init__(self, department_name)
        self.student_name = student_name
        self.age = age

    def get_student_info(self):
        # Hierarchical Inheritance: get_collage_info and get_department_info called from parent classes
        super().get_collage_info()
        super().get_department_info()
        print(f"Student name is {self.student_name} and age is {self.age}")


# Derived class representing a HybridStudent, inheriting from University and Student
class HybridStudent(University, Student):
    def __init__(self, university_name, collage_name, location, department_name, student_name, age):
        # Hybrid Inheritance: HybridStudent inherits from University and Student
        University.__init__(self, university_name)
        Student.__init__(self, collage_name, location, department_name, student_name, age)

    def get_hybrid_student_info(self):
        super().get_university_info()
        super().get_collage_info()
        super().get_department_info()
        print(f"Student name is {self.student_name} and age is {self.age}")


hybrid_std = HybridStudent("ABC University", "SPEC", "Anand", "IT", "Dhruvish Patel", 21)
hybrid_std.get_hybrid_student_info()
