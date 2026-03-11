# 3. Cree una clase de `User` que:
#     - Tenga un atributo de `date_of_birth`.
#     - Tenga un property de `age`.
    
#     Luego cree un decorador para funciones que acepten un `User` como parámetro que se encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.

from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth 
        
    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

def is_adult(func):
    def inner(user, *args, **kwargs):
        if user.age < 18:
            raise ValueError("User is not an adult.")
        return func(user, *args, **kwargs)
    return inner
    
    
@is_adult
def access_restricted_area(user):
    print("Access granted to restricted area." + "\n" + f"User age: {user.age}") 

u1 = User(date(2000, 5, 20))
access_restricted_area(u1)
u2 = User(date(2010, 7, 15))
access_restricted_area(u2)