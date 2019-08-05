class User:
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_profile = {}
        for key, value in user_info.items():
            self.user_profile[key] = value

    def describe_user(self):
        print("hello, my name is " + self.first_name.title() +
              self.last_name.title() + "!")
        print("and these are my additional information: ")
        for key, value in self.user_profile.items():
            print(key + ": " + str(value))

    def greet_user(self):
        print("welcome to join us, " + self.first_name.title() +
              self.last_name.title() + "!")

mike = User("mike", "evian", age=18, hobby="skiing")
penn = User("penn", "kevin", major="physics", location="boston")

mike.describe_user()
mike.greet_user()

penn.describe_user()
penn.greet_user()