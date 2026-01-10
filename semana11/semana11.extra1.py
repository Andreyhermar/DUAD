class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Value cannot be 0 or negative")
        
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (self.width + self.height) * 2
    
try:
    height = int(input("Insert the height: "))
    width = int(input("Insert the width: "))
    rectangle = Rectangle(width, height)

    print(rectangle.get_area())
    print(rectangle.get_perimeter())

except ValueError as e:
    print(e)