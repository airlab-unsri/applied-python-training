# Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass.

- **Common Superclass**:
  - Create a common superclass that defines shared methods or attributes.
- **Subclasses with Different Implementations**:
  - Subclasses provide their own implementations of methods.

**Example of polymorphism**:

```{code-block} python
# Common superclass
class Shape:
    def area(self):
        pass


# Subclasses with different implementations of area
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"Area: {shape.area()}")
```
