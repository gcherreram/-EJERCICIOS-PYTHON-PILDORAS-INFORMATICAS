# Caracteristicas que tienen los objetos, carros, motos, barcos, camiones, etc.
# Comportamiento en común que tienen todos los objetos, Arrancan, Freanan y Aceleran

class Vehiculos():

    def __init__(self,marca,modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(sekf):

        self.enmarcha=True

    def acelerar(self):

        self.acelera=True

    def frenar(self):
        self.frena=True

# Salto de linea \n

    def estado(self):
        print("Marca; ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
            self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena) 

class moto(Vehiculos):
    pass

miMoto=moto("Honda", "CBR")

miMoto.estado()

