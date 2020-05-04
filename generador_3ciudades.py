def devuelve_ciudades(*ciudades):      # El * delante del argumento de una funcion indica que va a recibir un numero indeterminado de argumentos, y en este caso en forma de tupla
    for elemento in ciudades:
        # for subElemento in elemento:
            yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))