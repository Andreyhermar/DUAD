# 1. Cree una clase base `Vehicle` con los atributos:
#     - `_brand`
#     - `_year`
# - Agregue un método `get_info()` que devuelva una descripción del vehículo.
# - Luego cree dos clases hijas:
#     - `Car`
#     - `Motorcycle`
# - Cada una debe agregar su propio atributo (por ejemplo, `doors` o `type`) y sobrescribir el método `get_info()` para incluir esta información adicional.
# - Ejemplo:
#     - Entrada:
        
#         ```python
#         vehicle1 = Car("Toyota", 2020, 4)
#         vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")
#         ```
        
#     - Salida:
        
#         ```python
        
#         print(vehicle1.get_info())  # Toyota (2020) - 4 puertas
#         print(vehicle2.get_info())  # Yamaha (2022) - Tipo: Deportiva
#         ```

class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    @property
    def brand(self):
        return self._brand
    
    @property
    def year(self):
        return self._year

    def get_info(self):
        return f"{self.brand} ({self.year})"

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors
    
    def get_info(self):
        return f"{super().get_info()} - {self.doors} doors"

class Motorcycle(Vehicle):
    def __init__(self, brand, year, moto_type):
        super().__init__(brand, year)
        self.moto_type = moto_type

    def get_info(self):
        return f"{super().get_info()} - {self.moto_type}"

vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "Sport")

print(vehicle1.get_info())  # Toyota (2020) - 4 puertas
print(vehicle2.get_info())  # Yamaha (2022) - Tipo: Deportiva