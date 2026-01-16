# Cree una clase abstracta de `Shape` que:
    # 1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
    # 2. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
    # 3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def calculate_perimeter(self):
        pass
        
    @abstractmethod
    def calculate_area(self):
        pass

# Area=π×r2 Perimetro=2×π×r
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2

# Area=lado2 Perimetro = 4×lado
class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def calculate_perimeter(self):
        return 4 * self.side
        
    def calculate_area(self):
        return self.side ** 2

# Area = base x Altura Perimetro = 2×(base+altura) 
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
    def calculate_area(self):
        return self.width * self.height
    

shapes = [
    Circle(5),
    Square(6),
    Rectangle(2,3)
]

for shape in shapes:
    print (f"Area = {shape.calculate_area()}")
    print (f"Perimeter = {shape.calculate_perimeter()}")


