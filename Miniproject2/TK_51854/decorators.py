from car import Car

# Base Decorator
class CarDecorator(Car):

    def __init__(self, car: Car):
        self._car = car

    def get_description(self):
        return self._car.get_description()

    def get_cost(self):
        return self._car.get_cost()


# Sunroof Feature
class Sunroof(CarDecorator):

    def get_description(self):
        return self._car.get_description() + ", Sunroof"

    def get_cost(self):
        return self._car.get_cost() + 50000


# Navigation System Feature
class Navigation(CarDecorator):

    def get_description(self):
        return self._car.get_description() + ", Navigation System"

    def get_cost(self):
        return self._car.get_cost() + 30000


# Leather Seats Feature
class LeatherSeats(CarDecorator):

    def get_description(self):
        return self._car.get_description() + ", Leather Seats"

    def get_cost(self):
        return self._car.get_cost() + 45000