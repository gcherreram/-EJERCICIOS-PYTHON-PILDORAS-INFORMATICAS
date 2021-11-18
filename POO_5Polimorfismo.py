class Coches():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")

# miVehiculo=Moto()
# miVehiculo.desplazamiento()

# miVehiculo2=Coches()
# miVehiculo2.desplazamiento()

# miVehiculo3=Camion()
# miVehiculo3.desplazamiento()

def desplazamientoVehiculo(Vehiculo):
    Vehiculo.desplazamiento()


miVehiculo=Camion()

desplazamientoVehiculo(miVehiculo)

