class Coche():
    largoChasis=250
    anchoChasis=120         # Propiedades
    ruedas=4
    enmarcha=False

    def arrancar(self):           #Comportamiento
        self.enmarcha=True
    
    def estado(self):              #Comportamiento
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche está parado"

miCoche=Coche()         #instanciar una clase
print("El largo del coche es: ",miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, " ruedas")
miCoche.arrancar()
print (miCoche.estado())

print("------------------A continuación creamos el segundo objeto---------------")

miCoche2=Coche()
print("El largo del coche es: ",miCoche2.largoChasis)
print("El coche tiene ", miCoche2.ruedas, " ruedas")
miCoche2.arrancar()
print (miCoche2.estado())

