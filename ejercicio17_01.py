

num1=int(input("Introduce un numero por favor: "))
num2=int(input("Introduce un numero mayor al anterior, por favor: "))

while num1<=num2:
    num1=num2
    num2=int(input("Introduce un numero mayor al anterior, por favor: "))

    if num1>num2:
        break