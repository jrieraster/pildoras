def generaPares(limite):
    num=1

   

    while num<limite:

        yield num*2     

        num=num+1

devuelvePares=generaPares(10)  # Genero una variable objeto, donde almaceno el objeto iterable que devuelve la función

# for i in devuelvePares:
#     print (i)

print(next(devuelvePares))      # Voy llamando al elemento de la lista que necesito y la función queda en 
                                # standby o  suspensión ahorrando recursos

print("Aquí podría ir más código....")

print(next(devuelvePares))

print("Aquí podría ir más código....")

print(next(devuelvePares))

print("Aquí podría ir más código....")