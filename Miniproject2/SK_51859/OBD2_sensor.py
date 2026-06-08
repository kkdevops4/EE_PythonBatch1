coolant_temp_sensor = [
    {"time": "0 min", "temp": 25, "state": "ambient_temp"},
    {"time": "2 min", "temp": 40, "state": "initial_warm_up"},
    {"time": "5 min", "temp": 60, "state": "engine_warming_faster"},
    {"time": "10 min", "temp": 80, "state": "approaching_operating_temp"},
    {"time": "15 min", "temp": 100, "state": "normal_operating_range"}
]

rules = {
    "ambient_temp": range(20, 31),
    "initial_warm_up": range(31, 51),
    "engine_warming_faster": range(51, 71),
    "approaching_operating_temp": range(71, 96),
    "normal_operating_range": range(96, 105)
}


class OBDReader:
    def check_signal(self, delay, file):
        if delay > 15:
            msg = "CRITICAL: No Signal From ECU"
            print(msg)
            file.write(msg + "\n")
            return False

        elif delay >= 10:
            msg = "WARNING: Signal Delay Detected"
            print(msg)
            file.write(msg + "\n")
            return True
        else:
            msg = "SUCCESS: Signal Received"
            print(msg)
            file.write(msg + "\n")
            return True

    def check_temperature(self, temp, state, file):
        valid_range = rules[state]
        low = valid_range.start
        high = valid_range.stop - 1

        if temp < low:
            msg = "ERROR: Temperature LOW " + str(temp) + "C for " + state
            print(msg)
            file.write(msg + "\n")
            return False

        elif temp > high:
            msg = "ERROR: Temperature HIGH " + str(temp) + "C for " + state
            print(msg)
            file.write(msg + "\n")
            return False

        else:
            msg = "SUCCESS: " + str(temp) + "C - ALL OK (" + state + ")"
            print(msg)
            file.write(msg + "\n")
            return True
        

reader = OBDReader()
file = open("obd_output.txt", "a")
for data in coolant_temp_sensor:
    print("\n-----------------------------")
    file.write("\n-----------------------------\n")

    delay = int(input("Enter ECU Delay (ms): "))
    signal_status = reader.check_signal(delay, file)
    if signal_status is False:
        stop_msg = "INFO: Monitoring Stopped"      
        break

    temp = int(input("Enter Coolant Temperature (C): "))
    temp_status = reader.check_temperature(temp, data["state"], file)

    if temp_status is False:
        stop_msg = "INFO: Monitoring Stopped Due To Temperature Error"
        break

end_msg = "INFO: Program Ended"
file.write(f"Delay Time: {delay} \nTemperature of Coolant Status{temp_status}")
file.close()