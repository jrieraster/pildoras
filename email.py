arroba=0
punto=0
miEmail=input("Introduce tu direccion de email: ")
for i in miEmail:
    if(i=="@"):
        arroba=arroba+1
    elif(i=="."):
        punto=punto+1
if punto>=1 and arroba==1:
        print("El Mails es correcto")
else:
        print("El mail no es correcto")
     