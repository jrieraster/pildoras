print("Promedio de numeros")

numero_1=int(input("Introduce el Primer Número "))

numero_2=int(input("Introduce el Segundo Número "))

numero_3=int(input("Introduce el Tercer Número "))

def promedio(n1,n2,n3):
    pro=(n1+n2+n3)/3
    print(f"El promedio de los numeros es: {pro}")

promedio(numero_1, numero_2, numero_3)
