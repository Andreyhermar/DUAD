nombre = input("Ingrese su nombre: \n")
apellido = input("Ingrese su apellido: \n")
edad = int(input("Ingrese su edad: \n"))

if edad < 2:
    categoria = "Bebe"
elif edad < 10:
    categoria = "Niño"
elif edad < 12:
    categoria = "Preadolecente"
elif edad < 18:
    categoria = "Adolescente"
elif edad < 30:
    categoria = "Adulto joven"
elif edad < 65:
    categoria = "Adulto"
else:
    categoria = "Adulto Mayor"

print(f"\nHola {nombre} {apellido}, tienes {edad} años y eres {categoria}.")