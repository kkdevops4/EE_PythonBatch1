# Basic details of ECU modules such as Engine ECU, ABS ECU and Airbag ECU :

class ECU:
    def __init__(self, ecu_id, ecu_type, manufacturer, software_version):
        self.ecu_id = ecu_id
        self.ecu_type = ecu_type
        self.manufacturer = manufacturer
        self.software_version = software_version


    def display_info(self):
        print(f"ECU ID: {self.ecu_id}")
        print(f"ECU Type: {self.ecu_type}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Software Version: {self.software_version}")
        print("-" * 35)


    def is_updated(self, latest_version):
        if self.software_version == latest_version:
            print(f"{self.ecu_type} ECU is up to date.")
        else:
            print(f"{self.ecu_type} ECU needs an update to (Latest: {latest_version}).")    



engine_ecu = ECU("ECU01", "Engine ECU", "Denso", "v3.1")
abs_ecu = ECU("ECU02", "ABS ECU", "Bosch", "v4.0")
airbag_ecu = ECU("ECU03", "Airbag ECU", "Continental", "v3.5")


engine_ecu.display_info()
abs_ecu.display_info()
airbag_ecu.display_info()


latest_version = "v4.0"
engine_ecu.is_updated(latest_version)
abs_ecu.is_updated(latest_version)
airbag_ecu.is_updated(latest_version)
