num1=(int(input("Introduce el Primer Número ")))

num2=(int(input("Introduce el Segundo Número ")))

def DevuelveMax(n1,n2):
    if n1 < n2:
        print(n2)
    elif n1 > n2:
        print (n1)
    else:
        print ("Son Iguales")
    
    print ("el numero más alto es: ")

DevuelveMax(num1, num2)
print("Fin del Programa")

