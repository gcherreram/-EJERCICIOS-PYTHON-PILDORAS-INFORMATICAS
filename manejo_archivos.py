# Manejo de flujo de información herramientas basicas
from io import open

archivo_texto=open("archivo.txt","r+") 

lista_texto=archivo_texto.readlines();

lista_texto[1]="Esta linea ha sido incluida desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()

# r+ significa lectura y escritura

# archivo_texto.seek(11) posiciona el puntero en el caracter 11

# archivo_texto.seek(len(archivo_texto.read())/2)

# print(archivo_texto.read())

# para situar al final de la primera linea o la linea que querramos
# archivo_texto.seek(len(archivo_texto.readline()))

#Si dentro del read colocamos un número, leera desde el inicio hasta la posición que ingresamos

# El segundo argumento dice como voy a abrir el archivo, en moto lectura read
# en modo escritura write
# En modo agregar sera 'a'

# ---------------------------------------------------

# archivo_texto=open("archivo.txt","w")

# frase ="Estupendo día para estudiar Python \nel lunes"

# archivo_texto.write(frase)

# archivo_texto.close()

#--------------------------------------------------------
# archivo_texto=open("archivo.txt","a")

# # texto=archivo_texto.read()

# # archivo_texto.close()

# # print(texto)

# # ---------------------------------------------------------

# # .readlines me permite listar las lineas del archivo

# # lineas_texto=archivo_texto.readlines()

# # archivo_texto.close

# # print(lineas_texto)

# # puedes imprimir lineas exactas con print(lineas_texto[1]) cambiar el
# # número permitira ingresar a la linea que quieras

# # ---------------------------------

# archivo_texto.write("\nSiempre es una buena ocasión para estudiar python")

# archivo_texto.close

