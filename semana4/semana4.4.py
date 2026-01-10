import random

secret = random.randint(1, 10)
#print(secret) #Just to check that the script successfully compares the secret and the guess

while True:
    try:
        guess = int(input("Adivine un numero del 1 al 10\n"))
        if guess < 1 or guess > 10:
            print("Por favor, ingrese un número entre 1 y 10.")
            continue
        if guess == secret:
            print("Felicidades, adivino el numero")
            break
        else:
            print("Intentelo de nuevo")
    except ValueError:  # Handle cases where the user enters a non-numeric value
        print("Entrada inválida. Por favor, ingrese un número entre 1 y 10.")