# Parent class
class Animal:
    def __init__(self, name):
        print(f"Initializing animal named {name}")
        self.name = name

    def speak(self):
        pass


# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"


class Cat(Animal):
    def __init__(self, name, race):
        super().__init__(name)
        self.race = race
        print(f"Initializing cat named {self.name} of {self.race} race")

    def speak(self):
        return f"{self.name} says meong!"


my_dog = Dog("Buddy")
print(my_dog.speak())  # Calls the speak method of the Dog class

my_cat = Cat("Ocong", "Persian")
print(my_cat.speak())
