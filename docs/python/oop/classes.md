# Classes

**Example of creating a simple class and an object:**

```{code-block} python
# Define a simple class
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")


# Create an object (instance) of the Dog class
my_dog = Dog("Buddy")
my_dog.bark()  # Call the bark method on the object
```

## Class Attributes and Methods

Classes can have attributes and methods that define their behavior.

- **Class Attributes**:
  - Class attributes are shared among all instances of the class.
- **Instance Attributes**:
  - Instance attributes are specific to individual objects.
- **Methods**:
  - Methods are functions defined within a class.

**Example of class attributes and methods:**

```{code-block} python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2

    def circumference(self):
        return 2 * 3.14159 * self.radius


my_circle = Circle(5)
print(f"Area: {my_circle.area()}")
print(f"Circumference: {my_circle.circumference()}")
```

## Python Documentation

- [Classes](https://docs.python.org/3/tutorial/classes.html)
