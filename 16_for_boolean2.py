contador=0
miEmail=input("Introduce tu direccion de email: ")
for i in miEmail:
    if(i=="@" or i=="."):
        contador=contador+1
if contador>=2:
        print("El Mails es correcto")
        print(contador)
else:
        print("El mail no es correcto")
        print(contador)