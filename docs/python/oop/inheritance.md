# Inheritance

Inheritance allows you to create new classes that inherit attributes and methods from existing classes.

- **Parent Class (Superclass)**:
  - The parent class defines common attributes and methods.
- **Child Class (Subclass)**:
  - The child class inherits from the parent class and can have additional attributes and methods.

**Example of inheritance**:

```{code-block} python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"


my_dog = Dog("Buddy")
print(my_dog.speak())  # Calls the speak method of the Dog class
```

## Mixins (multiple inheritance)

Python allows you to inherit from multiple classes. While the technical term for this is multiple inheritance, many developers refer to the use of more than one base class adding a mixin. These are commonly used in frameworks such as [Django](https://www.djangoproject.com).

- [Multiple Inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
- [super](https://docs.python.org/3/library/functions.html#super) is used to give access to methods and properties of a parent class

**Example of multiple inheritance**:

```{code-block} python
class Loggable:
    def __init__(self):
        self.title = "

    def log(self):
        print("Log message from " + self.title)


class Connection:
    def __init__(self):
        self.server = "

    def connect(self):
        print("Connecting to database on " + self.server)


class SqlDatabase(Connection, Loggable):
    def __init__(self):
        super().__init__()
        self.title = "Sql Connection Demo"
        self.server = "Some_Server"


def framework(item):
    if isinstance(item, Connection):
        item.connect()
    if isinstance(item, Loggable):
        item.log()


sql_connection = SqlDatabase()
framework(sql_connection)
```

## Python Documentation

- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Multiple Inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
