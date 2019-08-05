class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print("this restaurant is called " + self.restaurant_name.title() +
              "and it features " + self.cuisine_type.title() + "food"
              + ", having served " + str(self.number_served) + " guests!")

    def open_restaurant(self):
        print("the restaurant " + self.restaurant_name.title() + " opens today!")

    def set_number_served(self, new_number):
        self.number_served = new_number

    def increment_number_served(self, increment_number):
        self.number_served += increment_number

my_restaurant = Restaurant("the secret garden", "mexican", 15)
my_restaurant.set_number_served(27)
my_restaurant.describe_restaurant()

my_restaurant.increment_number_served(13)
my_restaurant.describe_restaurant()