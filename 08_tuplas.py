miTupla=("Juan",13,7,1995)

print(miTupla)

print(miTupla[2])

miLista=list(miTupla) #"List" Asigno a una lista la tupla

print(miLista) #Notar que cambia los () por []

myList=["teto","Tito", False,5,18,21.9,18]

myTuple=tuple(myList) # "Tuple" Para convertir una lista a una tupla

print(myTuple)

print("teto" in myTuple)

print(myTuple.count(18)) # Cuenta cuanta vces esta el valor "18"

print(len(myTuple))

tuplaUni=("Juan",) # Esto es oara definir unta tupla unitaria. Prestarle atención a la ","

print(len(tuplaUni))

tuplaSin="pepo", 13, 8, 9.8 # Poner una tupla sin parentesis se denomina "empaquetado de tupla"

print(tuplaSin)

