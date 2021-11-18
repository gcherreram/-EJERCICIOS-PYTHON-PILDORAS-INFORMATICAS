import re

# nombre1="sandra López"
# nombre2="Antonio Gómez"
# nombre3="sandra López"

# if re.match("Sandra", nombre3, re.IGNORECASE):

#     print ("Hemos encontrado el nombre")

nombre1="Jara López"
nombre2="Antonio Gómez"
nombre3="Lara López"

# if re.match(".ara", nombre3, re.IGNORECASE):

#     print ("Hemos encontrado el nombre")

# else:

#     print("No hemos encontrado el nombre")

# cadena1="Jara López"
# cadena2="5628491"
# cadena3="a59851264"

# # \d es para ver si comienza con  un digito

# if re.match("\d", cadena2):

#     print ("Hemos encontrado el número")

# else:

#     print("No hemos encontrado el número")

# función search busca en toda la cadena de texto

if re.search("López", nombre1, re.IGNORECASE):

    print ("Hemos encontrado el nombre")

else:

    print("No hemos encontrado el nombre")