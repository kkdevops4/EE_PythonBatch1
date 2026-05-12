
import os
 
# -----------------------------
# STEP 1: Create files if not exist
# -----------------------------
if not os.path.exists("firmware_v1.txt"):
    with open("firmware_v1.txt", "w") as f:
        f.write("Version 1.0")
 
if not os.path.exists("firmware_v2.txt"):
    with open("firmware_v2.txt", "w") as f:
        f.write("Version 2.0")
 
if not os.path.exists("ecu_current.txt"):
    with open("ecu_current.txt", "w") as f:
        f.write("Version 1.0")
 
 
# -----------------------------
# STEP 2: ECU Context Manager
# -----------------------------
class ECU:
    def __enter__(self):
        print("\nStarting ECU update...")
 
        with open("ecu_current.txt", "r") as f:
            self.before_update = f.read()
 
        print("Current firmware:", self.before_update)
        return self
 
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("Update failed:", exc_value)
 
            # rollback → Version 1.0
            with open("firmware_v1.txt", "r") as f:
                safe_version = f.read()
 
            with open("ecu_current.txt", "w") as f:
                f.write(safe_version)
 
            print("Rollback performed → Version 1.0")
 
        else:
            print("Update successful!")
 
        # show final state
        with open("ecu_current.txt", "r") as f:
            print("Final firmware:", f.read())
 
        print("Exiting ECU update\n")
 
        return True  # suppress crash
 
 
# -----------------------------
# STEP 3: Firmware Update Logic
# -----------------------------
def update_firmware():
    try:
        with ECU():
            choice = input("Enter 0 for SUCCESS (v2.0), 1 for FAIL (rollback): ")
 
            if choice == "1":
                raise Exception("Simulated update failure")
 
            # SUCCESS → write Version 2.0
            with open("firmware_v2.txt", "r") as f:
                new_version = f.read()
 
            with open("ecu_current.txt", "w") as f:
                f.write(new_version)
 
            print("Firmware updated to Version 2.0")
 
    except Exception as e:
        print("Handled outside error:", e)

        
 
# -----------------------------
# RUN PROGRAM
# -----------------------------
update_firmware()
 
 