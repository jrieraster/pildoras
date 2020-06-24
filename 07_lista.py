miLista=["Maria", "Pepe", "MArta", "Antonio"]

print(miLista[:]) #Imprime la lista entera

print(miLista[3]) #Imprime el indice 3 de la lista

print(miLista[0:2]) #Imprime desde el indice 0 (incluido) hasta el indice 2 (no incluido)

print(miLista[1:]) #Imprime a partir del indice 1

print(miLista[:2]) #Imprime hasta el indice 2 (no incluido)


miLista.append("Sandra") #Agregamos un indice al final

print(miLista[:])

miLista.insert(2,"Tito") # Insertamos en la posición 3 a Tito

print(miLista[:])

miLista.extend(["Tati","Toto","Teto"]) # Concatena otra lista

print(miLista[:]) #Imprime la lista entera

print(miLista.index("Tito")) # Imprime el número de indice de Tito

print(miLista.index("Teto")) # Imprime el número de indice de Teto

print("Tati" in miLista) # Imprime si esta o no en la lista 

myList=["Maria", 5, True, 78.35]

print(myList[:])

myList.remove(True) # Indico que elemneto deseo eliminar

print(myList[:])

myList.pop() # Elimina el ultimo elemento de la lista

print(myList[:])

totalList=miLista+myList

print(totalList[:])

