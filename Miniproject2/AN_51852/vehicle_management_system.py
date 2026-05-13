import json #Python objects ↔ JSON text
from tabulate import tabulate #Import only the tabulate function from the tabulate package.


class Vehicle:
    def __init__(self, vin, customer_name, model, color): #These are future instructions.
        self.vin = vin
        self.customer_name = customer_name
        self.model = model
        self.color = color #Store the passed color inside this object self.color

    def to_dict(self): #Convert object → dictionary.
        return {  #why return here? returns this dict to the method to_dict
            "vin": self.vin,
            "customer_name": self.customer_name,
            "model": self.model,
            "color": self.color
        }

    def display(self):
        table = [[self.vin, self.customer_name, self.model, self.color]]  #Build Inner List and Wrap in Outer List because Each inner list = one table row.
        print(tabulate(table, headers=["VIN", "Customer", "Model", "Color"], tablefmt="grid")) #Use "grid"-style table formatting.


# load data from file
def load_data():
    try: #Attempt this code. If error happens, jump to except block.
        with open("vehicles.json", "r") as file: #open "vehicles.json" file in read mode in the name file, file closed automatically after it ends
            data = json.load(file) #Converts JSON text → Python objects
            vehicles = [] #Creates empty list
            for item in data: #Loop runs once. Take each dictionary from data one at a time.”
                vehicle = Vehicle(
                    item["vin"], #finds key "vin", gets value "123", Same for others.
                    item["customer_name"],
                    item["model"],
                    item["color"]
                )#Dictionary lookup and resturns thier respective values
                vehicles.append(vehicle) #before vehicles = [] now, vehicles = [vehicle_object]
            return vehicles #Function sends list back to caller, Execution immediately exits function.
    except FileNotFoundError: #If file missing:
        return []  #Program safely starts with empty data. 
    except json.JSONDecodeError:
        print("File is corrupted!")
        return []


# save data to file
def save_data(vehicles):
    data = [] #data is empty list now
    for vehicle in vehicles: #runs loop once on line 30 vehicles class (object list)
        data.append(vehicle.to_dict()) #first Returns dictionary then appends to list(empty at line 49) to_dict line 12, call vehicle.to_dict(),returns dictionary, append dictionary to list 
    with open("vehicles.json", "w") as file: #Existing file contents are erased first then 
        json.dump(data, file, indent=4) #for spacing, Python converts Python list/dict to JSON text
        #Take Python data and dump it into a file.


# add vehicle
def add_vehicle(vehicles): #inherited from class vehicles
    while True: #Infinite loop begins and stop at break.
        vin = input("Enter VIN: ")
        if len(vin) == 17:
            break #if length of the VIN no. is 17(TRUE) then executes, Loop exits.
        print("VIN must be exactly 17 digits!") #If (FALSE) prints error and loop repeats.
    for vehicle in vehicles:
        if vehicle.vin == vin: #Duplicate Check, if input vin is equal to vin inside class vehicle, Python compares character-by-character internally.
            print("VIN already exists!")
            return #if found returns to caller
    customer_name = input("Enter customer name: ")
    while True:
        model = input("Enter model (Innova, Prius): ").strip().lower() #Removes outer spaces eg. "  PRIUS " to "PRIUS", lower makes all charcters lowercase eg. "PRIUS" to "prius"
        if model in ["innova", "prius"]: #if "prius" in ["innova", "prius"] ie ("prius" == "innova") or ("prius" == "prius"), False or True, since or operator TRUE
            model = model.capitalize() #"prius".capitalize() is "Prius"
            break
        print("Please enter model from given options!")

    while True: #same logic as model input and validation.
        color = input("Enter color (Red, White, Black): ").strip().lower()
        if color in ["red", "white", "black"]:
            color = color.capitalize()
            break
        print("Please enter color from given options!")
    vehicle = Vehicle(vin, customer_name, model, color) #Object created with these values. Triggers constructor.
    vehicles.append(vehicle) #List grows as the new values are added to the end of class. Vehicle stored in memory.
    save_data(vehicles) #File updated permanently, Writes updated list to JSON file.
    print("Vehicle added successfully!")


# view vehicles
def view_vehicles(vehicles):
    if not vehicles: #if vehicles is empty, not [] empty is True (because [] is False ) so it prints No vehicles found! and returns.
        print("No vehicles found!")
        return
    table = [] #here [] acts like False, So not [] is True 
    for vehicle in vehicles:
        table.append([ 
            vehicle.vin,
            vehicle.customer_name,
            vehicle.model,
            vehicle.color
        ]) #adds table values to the empty table, row by row 
    print(tabulate(table, headers=["VIN", "Customer", "Model", "Color"], tablefmt="grid")) #refer line 22


# search vehicle
def search_vehicle(vehicles):
    vin = input("Enter VIN to search: ")
    for vehicle in vehicles:
        if vehicle.vin == vin:
            vehicle.display() #calls def display(self): which shows the value in table form.
            return
    print("Vehicle not found!")


# update vehicle
def update_vehicle(vehicles):
    vin = input("Enter VIN to update: ")
    for vehicle in vehicles:
        if vehicle.vin == vin:
            print("Leave field empty if you don't want to change it.") #eg. if we want to keep new-name same as old one,press enetr,  new_name = "" ie empty string, 
            new_name = input("Enter new customer name: ")
            new_model = input("Enter new model: ")
            new_color = input("Enter new color: ")
            if new_name:
                vehicle.customer_name = new_name #If user presses ENTER: new_name = "", Empty string = False. So update skipped. if user eneters "Abc" ie new_name = "Abc" which is TRUE, thus vehicle.customer_name = new_name 
                pass 
            if new_model:
                vehicle.model = new_model #when user enters value, Non-empty string = True. Update occurs by savving ther new_value to old_value.
                pass 
            if new_color:
                vehicle.color = new_color
                pass 
            save_data(vehicles)
            print("Vehicle updated successfully!")
            return
    print("Vehicle not found!")


# delete vehicle
def delete_vehicle(vehicles):
    vin = input("Enter VIN to delete: ")
    for vehicle in vehicles:
        if vehicle.vin == vin:
            vehicles.remove(vehicle) #Removes matching object from list. Find the first matching element in the list and delete it.
            save_data(vehicles)
            print("Vehicle deleted successfully!")
            return
    print("Vehicle not found!")


# main menu
def menu():
    vehicles = load_data() #Loads all saved vehicles at startup.
    while True: #Menu repeats forever until break.
        print("\n===== VEHICLE MANAGEMENT SYSTEM =====")
        print("1. Add Vehicle")
        print("2. View Vehicles")
        print("3. Search Vehicle")
        print("4. Update Vehicle")
        print("5. Delete Vehicle")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_vehicle(vehicles)
        elif choice == "2":
            view_vehicles(vehicles)
        elif choice == "3":
            search_vehicle(vehicles)
        elif choice == "4":
            update_vehicle(vehicles)
        elif choice == "5":
            delete_vehicle(vehicles)
        elif choice == "6":
            print("Exiting...!")
            break
        else:
            print("Invalid choice!")


menu()