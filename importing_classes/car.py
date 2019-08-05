"""a class that can be represented as a car"""

class Car:
    """a simple attempt to represent a car"""
    def __init__(self, make , model, year, odometer_reading=0):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading

    def get_descriptive_name(self):
        """return a neatly formatted descriptive name"""
        long_name = str(self.year) +" " + self.make + " " +self.model
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's mileage"""
        print("this car has " + str(self.odometer_reading) +" miles on it.")

    def update_odometer(self, mileage):
        """set the odometer reading to the given value
        reject teh change if it attempts to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can not roll back the odometer!")

    def increment_odometer(self, miles):
        """add the given amount to the odometer reading"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """simulating filling gas tanks"""
        print("filling gas tanks")

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