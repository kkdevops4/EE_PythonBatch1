from abc import ABC, abstractmethod

# Abstract Car class
class Car(ABC):

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


# Concrete Base Car
class BasicCar(Car):

    def get_description(self):
        return "Basic Car"

    def get_cost(self):
        return 500000  # Base price in INR