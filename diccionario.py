midiccionario={"Alemania":"Berlin", "Francia":"Paris", "España":"Madrid", "Italia":"Roma"}

print(midiccionario["Italia"])

print(midiccionario)

midiccionario["Portugal"]="Londres" # Agregar elemento del diccionario

print(midiccionario)

midiccionario["Portugal"]="Lisboa" # Corregir valor del diccionario (acordarse clave:valor)

print(midiccionario)

del midiccionario["Alemania"] # Para eleminar el valor Berlin

print(midiccionario)

mydictio={"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}

print(mydictio)

mitupla=["España","Francia","Argentina","Alemania"]
midiccio={mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Baires", mitupla[3]:"Berlin"}
print(midiccio)

diccio_MJ={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991,1992,1993,1996,1997,1998]}
print(diccio_MJ)
print(diccio_MJ["anillos"])

print(diccio_MJ.keys())
print(diccio_MJ.values())
print(len(diccio_MJ))
