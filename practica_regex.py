import re

lista_nombres=['Ana',
                'Pedro',
                'María',
                'Rosa',
                'Sandra',
                'Celia']

for elemento in lista_nombres:
    if re.findall('[o-t]', elemento):

        print(elemento)

# Case sensitive, diferencia entre minusculas y mayusculas

for elemento in lista_nombres:
    if re.findall('Ma[0-3A-B]', elemento):

# Busca que comiencen por determinada pablabra

for elemento in lista_nombres:
    if re.findall('Ma[.:]', elemento):