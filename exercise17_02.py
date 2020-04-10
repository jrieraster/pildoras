numero=int(input("Introduce un numero: "))
suma=0

while numero > 0:
    suma=suma+numero
    numero=int(input("Introduce otro numero: "))

print( "La suma de los numeros introducidos es", str(suma))