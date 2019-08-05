class User:
    def __init__(self, first_name, last_name,):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("hello, my name is " + self.first_name.title() + " " +
              self.last_name.title() + "!")

    def greet_user(self):
        print("welcome to join us, " + self.first_name.title() +
              self.last_name.title() + "!")

class Admin(User):
    def __init__(self, first_name, last_name,):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

class Privileges:
    def __init__(self):
        self.privileges = ["can delete post", "can ban user", "can add post"]

    def show_privileges(self):
        print("your privileges are as follows:")
        for privilege in self.privileges:
            print(privilege)
