
contador_de_nota = 1
nota_actual = 0
cantidad_de_notas_aprobadas = 0
cantidad_de_notas_desaprobadas = 0
promedio_de_notas_aprobadas = 0 
promedio_de_notas_desaprobadas = 0
promedio_de_notas_total = 0

total_de_notas = int(input("Insert the number of grades to evaluate:\n"))

while contador_de_nota <= total_de_notas:
    nota_actual = int(input(f"Ingrese la nota número {contador_de_nota}: "))
    if nota_actual < 70:
        cantidad_de_notas_desaprobadas +=1
        promedio_de_notas_desaprobadas += nota_actual
    else:
        cantidad_de_notas_aprobadas +=1
        promedio_de_notas_aprobadas += nota_actual
    
    promedio_de_notas_total = promedio_de_notas_total + (nota_actual / total_de_notas)
    contador_de_nota +=1

#this code was written to avoid division between 0 when average is 0 on any of the grades.
if cantidad_de_notas_aprobadas > 0:
    promedio_de_notas_aprobadas /= cantidad_de_notas_aprobadas
else:
    promedio_de_notas_aprobadas = 0

if cantidad_de_notas_desaprobadas > 0:
    promedio_de_notas_desaprobadas /= cantidad_de_notas_desaprobadas
else:
    promedio_de_notas_desaprobadas = 0

#promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas / cantidad_de_notas_desaprobadas
#promedio_de_notas_aprobadas = promedio_de_notas_aprobadas / cantidad_de_notas_aprobadas

print("the student has the following number of grades approved: ", cantidad_de_notas_aprobadas, "\n")
print("This is the average of approved grades: ", promedio_de_notas_aprobadas, "\n")
print("This is the number of unapproved grades: ", cantidad_de_notas_desaprobadas, "\n")
print("This is the average of unapproved grades: ", promedio_de_notas_desaprobadas, "\n")
print("This is the total averaged of grades: ", promedio_de_notas_total, "\n")
