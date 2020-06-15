class Coche():

    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120         # Propiedades
        self.__ruedas=4             #Encapsulamos el dato para que no sea aacsible desde fuera
        self.__enmarcha=False

    def arrancar(self,arrancamos):           #Comportamiento
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche está parado"

          
    def estado(self):              #Comportamiento
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

miCoche=Coche()         #instanciar una clase

print(miCoche.arrancar(True))
miCoche.estado()

print("------------------A continuación creamos el segundo objeto---------------")

miCoche2=Coche()

print(miCoche2.arrancar(False))
miCoche2.__ruedas=2
miCoche2.estado()

