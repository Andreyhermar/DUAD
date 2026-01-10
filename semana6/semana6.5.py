def cap_function(text):
    capital_letter = 0
    lower_case = 0

    for caracter in text: 
        if caracter.isupper():
            capital_letter += 1
        elif caracter.islower():
            lower_case += 1
    
    print(f"El Numero de mayusculas es: {capital_letter}")
    print(f"El Numero de minusculas es: {lower_case}")
cap_function("Hello World")