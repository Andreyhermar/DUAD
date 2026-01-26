# 2. Cree una función que se llame `multiply`, la cual obtiene dos valores y los multiplica entre si
# - A esta función  se le debe combinar dos decoradores:
#     - `@log_call`: imprime el nombre de la función, los argumentos, fecha actual y el retorno
#     - `@validate_numbers`: revisa que todos los argumentos sean numéricos
#     - Ejemplo:
#         - Entrada:

#             multiply(3, 4)

#         - Salida:
            
#             "func:multiply - args: 3, 4 - [2025-07-17 14:00:00.000000] - Resultado: 12"
#             "Resultado 12"

from datetime import datetime

def log_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        current_time = datetime.now()
        print(f"Func: {func.__name__} - args: {', '.join(map(str, args))} - [{current_time}] - Result: {result}")
    return wrapper

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"{arg} is not a number.")
        return func(*args, **kwargs)
    return wrapper

            
@validate_numbers
@log_call
def multiply(a, b):
    return a * b

multiply(2,3)
multiply("a", "b")