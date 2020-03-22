print("Programa de evaluación de notas de alumnos")

nota_alumno=input("Introduce la nota del alumno: ") #Recordar que los valores introducidos en "input" para Python es texto

def evaluacion(nota):
    valoracion="aprobado"      # Recordar que la variable "valoracion" solo es accesible dentro de su ambito
    if nota<5:
        valoracion="suspenso"
    return valoracion

print(evaluacion(int(nota_alumno))) # Debemos modificar el valor introducido para que sea numérico mediante "int"