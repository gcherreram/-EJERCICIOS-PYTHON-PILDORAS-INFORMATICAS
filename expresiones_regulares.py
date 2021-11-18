import re

# cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

# # print(re.search("aprenderr",cadena))

# textoBuscar="Python"

# # textEncontrado=re.search(textoBuscar,cadena)

# # if re.search(textoBuscar,cadena) is not None:

# #     print("He encontrado el texto")

# # else: 

# #     print("No he encontrado el texto")

# # print(textEncontrado.start())

# # print(textEncontrado.end())

# # print(textEncontrado.span())

# print(len(re.findall(textoBuscar,cadena)))

# lista_nombres=['http://informaticaenespaña.es',
#                 'http://pildorasinformaticas.es',
#                 'http://pildorasinformaticas.com']

# for elemento in lista_nombres:
#     # if re.findall('es$', elemento): Revisa si los elementos terminan por
#     # if re.findall('^ftp', elemento): Revisa si los elementos comienzan por
#     if re.findall('[ñ]', elemento): 
#     # revisa si existen los caracteres en algun elemento
#         print(elemento)

lista_nombres=['hombres',
                'mujeres',
                'mascotas',
                'niños',
                'niñas']

for elemento in lista_nombres:
    if re.findall('niñ[oa]s', elemento):

        print(elemento)
