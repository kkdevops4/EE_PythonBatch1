from car import BasicCar
from decorators import Sunroof, Navigation, LeatherSeats


def show_menu():
    print("\nAvailable Features:")
    print("1. Sunroof (+50000)")
    print("2. Navigation System (+30000)")
    print("3. Leather Seats (+45000)")
    print("4. Finish Configuration")


def apply_feature(choice, car):
    if choice == "1":
        return Sunroof(car)
    elif choice == "2":
        return Navigation(car)
    elif choice == "3":
        return LeatherSeats(car)
    else:
        return car


def build_vehicle():
    car = BasicCar()

    print("🚗 Welcome to Vehicle Config Builder 🚗")
    print("--------------------------------------")
    print("Base Model:", car.get_description())
    print("Base Price:", car.get_cost(), "INR")

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "4":
            break

        if choice not in ["1", "2", "3"]:
            print("❌ Invalid choice! Try again.")
            continue

        car = apply_feature(choice, car)

        print("\n✅ Feature Added!")
        print("Current Configuration:", car.get_description())
        print("Current Cost:", car.get_cost(), "INR")

    print("\n🎉 Final Vehicle Configuration:")
    print("Description:", car.get_description())
    print("Total Cost:", car.get_cost(), "INR")


if __name__ == "__main__":
    build_vehicle()