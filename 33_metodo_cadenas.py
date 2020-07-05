# nombreUsuario=input("Introduce tu nombre de Usuario: ")

# print("El nombre es: ", nombreUsuario.upper())


# nombreUsuario=input("Introduce tu nombre de Usuario: ")

# print("El nombre es: ", nombreUsuario.capitalize())


edad=input("Introduce la edad: ")

while(edad.isdigit()==False):
    print("Por favor introduce un valor numerico")
    edad=input("Introduce la edad: ")


if (int(edad)<18 or int(edad)>100):
    print("No puede pasar")
else:
    print("Puedes pasar")


print(edad.isdigit())