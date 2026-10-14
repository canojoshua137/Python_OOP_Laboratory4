
from abc import ABC, abstractmethod

# Abstraction
class Vehicle(ABC):
    # Encapsulation
    def __init__(self, brand, speed):
        self.brand = brand
        self.__speed = speed

    @abstractmethod
    def start(self):
        pass

# Inheritance
class Car(Vehicle):
    # Polymorphism
    def start(self):
        print("Car engine is starting.")

# Create objects
vehicle = Car("Toyota", 120)

print("Vehicle is starting.")
vehicle.start()
