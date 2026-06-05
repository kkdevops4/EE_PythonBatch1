class BCMValidator:

    @staticmethod
    def validate(row):

        action = str(row["User_action"]).strip().lower()

        speed = row["Vehicle_Speed_ (km/h)"]

        driver = str(row["Driver_Door"]).strip().title()
        passenger = str(row["Passenger_Door"]).strip().title()
        rear_left = str(row["Rear_Left_Door"]).strip().title()
        rear_right = str(row["Rear_Right_Door"]).strip().title()
        boot = str(row["Boot_Door"]).strip().title()

        remarks = []

        if driver == "Open":
            remarks.append("Driver Door Open")

        if passenger == "Open":
            remarks.append("Passenger Door Open")

        if rear_left == "Open":
            remarks.append("Rear Left Door Open")

        if rear_right == "Open":
            remarks.append("Rear Right Door Open")

        if boot == "Open":
            remarks.append("Boot Door Open")

        all_closed = (
            driver == "Closed"
            and passenger == "Closed"
            and rear_left == "Closed"
            and rear_right == "Closed"
            and boot == "Closed"
        )

        if action == "lock_keyfob":

            if all_closed:
                actual = "Door Locked"
                remarks.append("Lock Successful")
            else:
                actual = "Door Unlocked"
                remarks.append("Lock Failed")

        elif action == "unlock_keyfob":

            actual = "Door Unlocked"
            remarks.append("Unlock Successful")

        elif action == "central_lock":

            if all_closed:
                actual = "Door Locked"
                remarks.append("Central Lock Successful")
            else:
                actual = "Door Unlocked"
                remarks.append("Central Lock Failed")

        elif action == "central_unlock":

            if speed <= 60:
                actual = "Door Unlocked"
                remarks.append("Unlock Allowed")
            else:
                actual = "Door Locked"
                remarks.append("Vehicle Speed Above Limit")

        elif action == "auto_lock":

            if speed >= 20:
                actual = "Door Locked"
                remarks.append("Auto Lock Activated")
            else:
                actual = "Door Unlocked"
                remarks.append("Speed Below Auto Lock Threshold")

        else:

            actual = "Invalid Action"
            remarks.append("Unknown Action")

        return actual, ", ".join(remarks)