# for letra in "Python":
    
#     if letra=="h":
#         continue        # Salta la siguiente instrucción, en este caso el print
#     print("Viendo la letra: " + letra)



nombre="Pildoras Informaticas"

contador=0
for i in nombre:
    if i!=" ":
        contador+=1         # esta instrucción es igual a contador=contador+1
    else: 
        continue

print(contador)


class MiClase:
    pass # para implementar mas tarde

print("es cualquiera pass")