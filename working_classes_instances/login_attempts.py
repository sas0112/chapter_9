class User:
    def __init__(self, first_name, last_name, login_attempts=0, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_profile = {}
        for key, value in user_info.items():
            self.user_profile[key] = value
        self.login_attempts = login_attempts

    def describe_user(self):
        print("hello, my name is " + self.first_name.title() +
              self.last_name.title() + "!")
        print("and these are my additional information: ")
        for key, value in self.user_profile.items():
            print(key + ": " + str(value))

    def greet_user(self):
        print("welcome to join us, " + self.first_name.title() +
              self.last_name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


mike = User("mike", "evian", )

mike.increment_login_attempts()
mike.increment_login_attempts()
mike.increment_login_attempts()
mike.increment_login_attempts()
mike.increment_login_attempts()

print(mike.login_attempts)
mike.reset_login_attempts()

print(mike.login_attempts)