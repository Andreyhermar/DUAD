# 1. string + string
print("Hola" + "Mundo")
#Resultado: HolaMundo

# 2. string + int
#print("Hola" + 5) 
#    print("Hola" + 5) # TypeError
#         ~~~~~~~^~~
#TypeError: can only concatenate str (not "int") to str

# 3. int + string
#print(5 + "Hola")
#print(5 + "Hola")
#      ~~^~~~~~~~
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 4. list + list
#print([1, 2, 3] + [4, 5, 6])  
#Resultado: [1, 2, 3, 4, 5, 6]

# 5. string + list → Error
#print("Hola" + [1, 2, 3])
#print("Hola" + [1, 2, 3])  # TypeError
#          ~~~~~~~^~~~~~~~~~~
#TypeError: can only concatenate str (not "list") to str

# 6. float + int → Suma normal (el resultado es float)
print(3.5 + 2)  # Resultado: 5.5

# 7. bool + bool → Los booleanos actúan como 1 y 0 en operaciones aritméticas
print(True + True) # Resultado: 2
print(True + False) #Resultado: 1
print(False + False) #Resultado: 0
