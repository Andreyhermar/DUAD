my_list = []
print("ingrese 10 valores y luego le mostraremos el valor mas alto")
for i in range(10):
    numero = int(input(f"ingrese el numero {i+1}: "))
    my_list.append(numero)
print("Los numeros ingresados son:", my_list)
highest_number = max(my_list)
print("El valor mas alto es: ", highest_number)