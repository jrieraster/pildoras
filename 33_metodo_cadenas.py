# nombreUsuario=input("Introduce tu nombre de Usuario: ")

# print("El nombre es: ", nombreUsuario.upper())


# nombreUsuario=input("Introduce tu nombre de Usuario: ")

# print("El nombre es: ", nombreUsuario.capitalize())


# edad=input("Introduce la edad: ")

# while(edad.isdigit()==False):
#     print("Por favor introduce un valor numerico")
#     edad=input("Introduce la edad: ")


# if (int(edad)<18 or int(edad)>100):
#     print("No puede pasar")
# else:
#     print("Puedes pasar")


# print(edad.isdigit())


email=input("Introduce tu email: ")

while(email.count("@")!=1):
    print("Por favor introduce un correo correcto")
    email=input("Introduce tu email: ")

while(email.count(".")==0):
    print("Por favor introduce un correo correcto")
    email=input("Introduce tu email: ")

while(email.endswith("@")==True):
    print("Por favor introduce un correo correcto")
    email=input("Introduce tu email: ")

while(email.startswith("@")==True):
    print("Por favor introduce un correo correcto")
    email=input("Introduce tu email: ")
print("La direccion de correo es correcta")

