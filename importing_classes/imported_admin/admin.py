from user import User

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