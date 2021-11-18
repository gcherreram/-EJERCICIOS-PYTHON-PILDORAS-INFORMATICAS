# clase 
# Una clase es el modelo 
# donde se redactan las caracteristicas comunes de un grupo de objetos.
# Coches

# Ejemplar de clase, instancia y objeto de clase
# Es una instancia de la clase, es un tipo de coche de una marca pero
# comparte la clase coche con otros más

# La modularización permite reutilizar trozos de código de un progrma
# en otro, se pueden tener varias clases en un código

# encapsulación: es proteger una propiedad para que no se pueda
# modificar desde fuera del constructor, se encapsula de dos raya al piso antecedida
# __

class Coche():

    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            return "El coche esta en marcha"

        else:

            return "El coche esta parado"

    def estado(self):
       print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ",
            self.__largoChasis)

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

miCoche2.ruedas=5

miCoche2.estado()