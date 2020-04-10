contra=input("Introduce la contraseña: ")

contador=0

for i in range(len(contra)):
    if contra[i]==" ":
        contador=1

if len(contra)<8 or contador>0:
    print("Contraseña erronea")

else:
    print("Contraseña Correcta")