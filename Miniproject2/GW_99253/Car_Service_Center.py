class Car:
    def __init__(self, car_name, owner, service_types):
        self.car_name = car_name
        self.owner = owner
        self.service_types = service_types

    def calculate_charge(self):
        total = 0
        for service in self.service_types:
            if service == "oil change":
                total += 1000
            elif service == "tyre rotation":
                total += 1500
            elif service == "full service":
                total += 5000
        return total

cars = []

for i in range(3):
    print(f"\nEnter details for Car {i+1}")
    
    car_name = input("Enter car name: ")
    owner = input("Enter owner name: ")
    
    service_input = input("Enter service types (oil change / tyre rotation / full service): ")
    service_list = [s.strip().lower() for s in service_input.split(",")]
    
    car = Car(car_name, owner, service_list)
    cars.append(car)


print("\n--- Service Details ---")

for car in cars:
    print("Owner Name:", car.owner)
    print("Car Name:", car.car_name)
    print("Service Types:", ", ".join(car.service_types))
    print("Total Charge:", car.calculate_charge())