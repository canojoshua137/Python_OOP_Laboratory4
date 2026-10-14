
from abc import ABC, abstractmethod

# Abstraction
class Student(ABC):
    def __init__(self, grade):
        # Encapsulation
        self.__grade = grade

    @abstractmethod
    def study(self):
        pass

# Inheritance
class CollegeStudent(Student):
    # Polymorphism
    def study(self):
        print("College student is studying programming.")

# Create a concrete Student class
class BasicStudent(Student):
    def study(self):
        print("Student is studying.")

# Create objects
student = BasicStudent(90)
college_student = CollegeStudent(95)

student.study()
college_student.study()
