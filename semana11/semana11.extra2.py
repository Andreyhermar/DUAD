class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    
    def accelerate(self, amount):
        if amount < 0:
            raise ValueError("The acceleration cannot be negative")
        self.speed += amount
    
    def brake(self, amount):
        if amount < 0:
            raise ValueError ("Braking cannot be negative")
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0

    def __str__(self):
        return f"{self.brand} {self.model} - Speed: {self.speed} km/h"
    
car1 = Car("BMW", "X5")
car1.accelerate(50)
print(car1)
car1.brake(20)
print(car1)