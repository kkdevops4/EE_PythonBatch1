def write_vehicle_info():
    """Write initial vehicle details to file"""
    filename = "vehicle_records.txt"
    
    print("=== VEHICLE SERVICE DESK ===")
    vin = input("Enter VIN: ").strip()
    owner = input("Enter Owner Name: ").strip()
    model = input("Enter Model: ").strip()
    year = input("Enter Year: ").strip()
    
    # Format: VIN | Owner | Model | Year
    record = f"{vin} | {owner} | {model} | {year}\n"
    
    # Creates file or overwrites
    with open(filename, "w") as f:
        f.write("VEHICLE SERVICE RECORDS\n")
        f.write("=" * 40 + "\n")
        f.write(record)
    
    print(f"Record saved to {filename}")

def append_vehicle_info():
    """Append new vehicle details without overwriting"""
    filename = "vehicle_records.txt"
    
    print("\n=== ADD NEW VEHICLE RECORD ===")
    vin = input("Enter VIN: ").strip()
    owner = input("Enter Owner Name: ").strip()
    model = input("Enter Model: ").strip()
    year = input("Enter Year: ").strip()
    
    # Format: VIN | Owner | Model | Year
    record = f"{vin} | {owner} | {model} | {year}\n"
    
    #  Adds to END without overwriting
    with open(filename, "a") as f:
        f.write(record)
    
    print(f" New record appended to {filename}")

def read_vehicle_records():
    """Read and display all records"""
    filename = "vehicle_records.txt"
    
    try:
        with open(filename, "r") as f:
            print("\n=== ALL VEHICLE RECORDS ===")
            print("-" * 40)
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(" No records found! Create first record.")

# === MAIN PROGRAM ===
while True:
    print("\n VEHICLE RECORDS SYSTEM")
    print("1. Write New File")
    print("2. Append Record")
    print("3. Read All Records")
    print("4. Exit")
    
    choice = input("Choose (1-4): ").strip()
    
    if choice == "1":
        write_vehicle_info()
    elif choice == "2":
        append_vehicle_info()
    elif choice == "3":
        read_vehicle_records()
    elif choice == "4":
        print(" Goodbye!")
        break
    else:
        print(" Invalid choice!")