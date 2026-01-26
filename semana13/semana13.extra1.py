# 1. Cree una función que imprima “Hola, [nombre]” dos veces:
# - Cree un decorador `@repeat_twice` que haga que la función decorada se ejecute dos veces seguidas, con los mismos argumentos
# - Ejemplo:
#     - Salida:
#         "Hola, Jeanca"
#         "Hola, Jeanca"

def repeat(n):
    def repeat_twice(func):
        def wrapper( *args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return repeat_twice

@repeat(2)
def salute(name):
    print(f"Hola, {name}")

salute("Andrey")