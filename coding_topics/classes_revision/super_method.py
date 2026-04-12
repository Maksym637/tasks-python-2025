class Bicycle:
    def start_journey(self):
        return "Journey started, happy cycling!"


class ElectricBicycle(Bicycle):
    def start_journey(self):
        return f"{super().start_journey()} The electric bicycle is ready!"


if __name__ == "__main__":
    my_ride = ElectricBicycle()
    print(my_ride.start_journey())
