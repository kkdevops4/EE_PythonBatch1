# Vehicle Registration System
from tabulate import tabulate
class Vehicle:
    def __init__(self, owner_name, company, model, year):
        self.owner_name = owner_name
        self.company = company
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, owner_name, company, model, year, num_doors):
        super().__init__(owner_name, company, model, year)
        self.num_doors = num_doors

class Bike(Vehicle):
    def __init__(self, owner_name, company, model, year, bike_type):
        super().__init__(owner_name, company, model, year)
        self.bike_type = bike_type

def save_vehicle(vehicle):
    with open("vehicles.txt", "a") as f:
        if type(vehicle) == Car:
            data = f"Car,{vehicle.owner_name},{vehicle.company},{vehicle.model},{vehicle.year},{vehicle.num_doors}\n"
        elif type(vehicle) == Bike:
            data = f"Bike,{vehicle.owner_name},{vehicle.company},{vehicle.model},{vehicle.year},{vehicle.bike_type}\n" 
        else:
            return
        f.write(data)
                  
def add_vehicle():
    v_type = input("Enter vehicle type (Car/Bike): ").lower()
    owner_name = input("Enter Owner name: ")
    company = input("Enter company name: ")
    model = input("Enter model: ")
    year = input("Enter year: ")

    if v_type == "car":
        doors = input("Enter number of doors: ")
        vehicle = Car(owner_name, company, model, year, doors)
        
        headers = ["Type", "Owner", "Company", "Model", "Year", "Doors"]
        table = [[v_type,owner_name,company,model,year,doors]]

    elif v_type == "bike":
        bike_type = input("Enter bike type (sports/cruiser/commuter): ")
        vehicle = Bike(owner_name, company, model, year, bike_type)
        
        headers = ["Type", "Owner", "Company", "Model", "Year", "Bike_Type"]
        table = [[v_type,owner_name,company,model,year,bike_type]]

    else:
        print("Invalid vehicle type!")
        return
    
    save_vehicle(vehicle)
    print("Vehicle Registered successfully!")
    print(tabulate(table, headers=headers, tablefmt="grid"))
    
def view_vehicles(): 
    with open("vehicles.txt", "r") as f:
        lines = f.readlines()
        
    table = []
    headers = ["Type", "Owner", "Company", "Model", "Year", "Doors/Bike type"]

    print("--- Vehicle Records ---")
    for line in lines:
        data = line.strip().split(",")
        table.append(data)
    print(tabulate(table, headers=headers, tablefmt="grid"))
        
def Run_program():
    while True:
        print(" Vehicle Registration System ")
        print("1. Vehicle Registration")
        print("2. View Registered Vehicles")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_vehicle()
        elif choice == "2":
            view_vehicles()
        elif choice == "3":
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Try again.")

Run_program()


    
