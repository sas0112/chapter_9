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

my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.increment_odometer(27)
my_new_car.read_odometer()