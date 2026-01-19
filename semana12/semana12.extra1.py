# 1. Cree una clase `Employee` con los siguientes requisitos:
#     - Atributos privados: `_name`, `_salary`
#     - Use `@property` y `@<atributo>.setter` para:
#         - Mostrar el nombre y el salario
#         - Validar que el salario nunca sea negativo
#     - Cree un método `promote` que aumente el salario un porcentaje definido
#     - Ejemplo:
#         - Entrada:
#             employee = Employee("Ana", 1000)
#             employee.promote(0.1)  # +10%
#         - Salida:
#             print(employee.salary)  # 1100

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError ("Salary should never be negative")
        self._salary = value

    def promote(self, percentage):
        if percentage == 0:
            raise ValueError("promotion percentage needs to be positive")
        self._salary += self._salary * percentage
        
employee = Employee("Ana", 1000)
employee.promote(0.1)

print(employee.salary, employee.name)