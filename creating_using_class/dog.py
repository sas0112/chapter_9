class Dog:
    """a simple attempt to model a dog"""

    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting!")

    def roll_over(self):
        """simulate rolling over in response to a command"""
        print(self.name.title() + " is now rolling over!")

my_dog = Dog("willie", 6)
your_dog = Dog("anny", 4)
print("my dog's name is " + my_dog.name.title() + ".")
print("my dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

print("\nyour dog's name is " + your_dog.name.title() + ".")
print("your dog is " + str(your_dog.age) + " years old.")

your_dog.sit()