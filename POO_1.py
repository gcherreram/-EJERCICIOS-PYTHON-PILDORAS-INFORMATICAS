# Nuestra clase tiene 4 propiedades

class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

# Nuestra clase tiene 2 comportamientos o metodos

    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos

        if(self.enmarcha):
            return "El coche esta en marcha"

        else:

            return "El coche esta parado"

    def estado(self):
       print("El coche tiene ", self.ruedas, " ruedas. Un ancho de ", self.anchoChasis, " y un largo de ",
            self.largoChasis)

miCoche=Coche()

# print("el largo del coche es: ", miCoche.largoChasis)
# print("el coche tiene: ", miCoche.ruedas, "ruedas")
print(miCoche.arrancar(True))

miCoche.estado()

print("----------A continuación creamos el segundo objeto---------------")

miCoche2=Coche()
# print("El largo del coche es: ", miCoche2.largoChasis)
# print("El coche tiene ", miCoche2.ruedas, " ruedas")
print(miCoche2.arrancar(False))
miCoche2.estado()





