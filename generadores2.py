#el asterisco indica que va a recibir varios elementos y que
# aún no sabemos cuantos, adicional a esto, que se ingresa como una tupla
#Este ejemplo no tiene alguna aplicación
# def devuelve_ciudades(*ciudades):
#     for elemento in ciudades:
#         for subElemento in elemento:
#             yield subElemento

# ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", " Valencia")

# print(next(ciudades_devueltas))

# print(next(ciudades_devueltas))

# simplificado queda así

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
            yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", " Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))