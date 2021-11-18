class Vehiculos():
    
    def __init__(self,marca,modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):

        self.enmarcha=True

    def acelerar(self):

        self.acelera=True

    def frenar(self):
        self.frena=True

# Salto de linea \n

    def estado(self):
        print("Marca; ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
            self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena) 

class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class moto(Vehiculos):
    
    hcaballito=""

    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):
        print("Marca; ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
            self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena, "\n", self.hcaballito)

# Si se hace una herencia de moto que adicional hereda de vehiculos, el estado
# sobreescrito prevalecera sobr el de la clase padre

class vElectricos(Vehiculos):

    def __init__(self, marca, modelo):
       
       super().__init__(marca, modelo)
       self.autonomia=100
       
    def cargarEnergia(self):
        self.cargando=True

miMoto=moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class BicicletaElectrica(vElectricos,Vehiculos):

    pass

miBici=BicicletaElectrica("Orbea", "Kalloy")



