edad=int(input("Introduce tu edad por favor: "))

while edad<3 or edad>100:
    print("Has introducido una edad incorrecta. Vuelve a intentarlo")
    edad=int(input("Introduce tu edad por favor: "))

print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante " + str(edad))
