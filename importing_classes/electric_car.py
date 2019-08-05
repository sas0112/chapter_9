from car import Car

class Battery:
    """a simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=70):
        """initializing attributes of batteries"""
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement describing  the battery size."""
        print("this car has a " + str(self.battery_size) + "-KWh battery")

    def get_range(self):
        """print a statement about the range this battery provides"""
        if self.battery_size == 70:
            ranges = 240
        elif self.battery_size ==85:
            ranges = 270

        message = "This car can approximately go" + str(ranges)
        message += " miles on a full charge"
        print(message)

class ElectricCar(Car):
    """represent aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """electric cars don't have gas tanks"""
        print("electric cars don't have gas tanks")

my_car = ElectricCar("BYD", "Qin", 2016)
print(my_car.get_descriptive_name())