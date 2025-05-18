numbers = [1, 2, 3, 4, 5, 6]

contador = 0  # variable global

def incrementar():
    global contador  # indicamos que queremos usar la variable global para poder accesar desde la funcion
    contador += 1
    print("Contador dentro de la función:", contador)

incrementar()
incrementar()
print("Contador fuera de la función:", contador)