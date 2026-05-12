from abc import ABC, abstractmethod

# Base ECU class
class ECU(ABC):

    @staticmethod
    @abstractmethod
    def module_id():
        pass

    @abstractmethod
    def send_message(self):
        pass


# Engine ECU
class EngineECU(ECU):

    @staticmethod
    def module_id():
        return 1

    def send_message(self):
        print("Engine ECU sending RPM data")


# Transmission ECU
class TransmissionECU(ECU):

    @staticmethod
    def module_id():
        return 2

    def send_message(self):
        print("Transmission ECU sending gear data")


# ABS ECU
class ABSECU(ECU):

    @staticmethod
    def module_id():
        return 3

    def send_message(self):
        print("ABS ECU sending wheel speed data")


# Example usage
if __name__ == "__main__":
    ecus = [EngineECU(), TransmissionECU(), ABSECU()]

    for ecu in ecus:
        print("Module ID:", ecu.module_id())
        ecu.send_message()