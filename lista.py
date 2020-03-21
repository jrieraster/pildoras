miLista=["Maria", "Pepe", "MArta", "Antonio"]

print(miLista[1:])

miLista.append("Sandra")

print(miLista[1:])

miLista.insert(2,"Tito") # Insertamos en la posición 3 a Tito

print(miLista[1:])

miLista.extend(["Tati","Toto","Teto"]) # Concatena otra lista

print(miLista[:]) #Imprime la lista entera

print(miLista.index("Tito"))

print(miLista.index("Teto")) # Imprime el número de indice de Teto

print("Tati" in miLista) # Imprime si esta o no en la lista 