# Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

def number_validation(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"Parameter {arg} is not a number.")
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise ValueError(f"Parameter {key} with value {value} is not a number.")
        return func(*args, **kwargs)
    return wrapper
    
@number_validation
def date_of_birth(day, month, year):
    print(f"{day}/{month}/{year}")

date_of_birth(15, 8, 1990)
date_of_birth(15, "August", 1990)