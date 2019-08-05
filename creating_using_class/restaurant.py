class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("this restaurant is called " + self.restaurant_name.title() +
              "and it features " + self.cuisine_type.title() + "food.")

    def open_restaurant(self):
        print("the restaurant " + self.restaurant_name.title() + " opens today!")

my_restaurant = Restaurant("the secret garden", "mexican")
your_restaurant = Restaurant("the jelly fish", "cuba")
his_restaurant = Restaurant("kalaage", "japan")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant.describe_restaurant()
his_restaurant.describe_restaurant()