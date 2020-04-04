email=False # Recordar que el False y el True van con la primer letra en mayuscula
miEmail=input("Introduce tu direccion de email: ")
for i in miEmail:
    if(i=="@"):
        email=True
if email==True:
        print("El Mails es correcto")
else:
        print("El mail no es correcto")

