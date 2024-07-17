# Define Class Person, Person is a parent class
class Person:

    # Define Attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Define Method
    def speak(self):
        if self.age < 10:
            print(f"Hello, my name is {self.name.capitalize()}, i'am a child")
        elif self.age <= 17:
            print(f"Hello, my name is {self.name.capitalize()}, i'am a teen")
        else:
            print(f"Hello, my name is {self.name.capitalize()}, i'am an adult")


# Define Class Friend, Friend is a child class
class Friend(Person):

    # Define Attribute
    def __init__(self, name, age, country):
        super().__init__(name, age) # This is inheritance from Person
        self.country = country # This is original attribute Friend

    # Define Method
    def speak(self):
        super().speak()
        print(f"I'am your friend from {self.country.capitalize()}")


name = input("What'y your name : ")
age = int(input("How old are you : "))
country = input("Where you came from : ")

print(10*"-")

myfriend = Friend(name, age, country)
myfriend.speak()