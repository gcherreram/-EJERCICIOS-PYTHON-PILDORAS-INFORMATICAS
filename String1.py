# Upper pone todo en mayuscula
# lower pone todo en minuscula
# capitalize, la primera letra del string la convierte a mayuscula
# count, cuenta cuantas veces aparece una letra o una cadena de caracteres
# find, devuelve la posición del caracter o el grupo
# isdigit, devuelve un booleano, indica si el caracter es un digito
# isalum, comprueba si es alpha numerico
# isalpha, si hay solo letras
# split, separa por espacios
# strip, borra los espacios sobrantes al principio o al final
# replace, reemplaza un caracter o un grupo de caracteres
# rfind, lo mismo que find pero inicia desde el final

# nombreUsuario=input("Introduce tu nombre de usuario: ")
# print("El nombre es: ", nombreUsuario.upper())

edad= input("Introduce la edad: ")

while(edad.isdigit())==False:
    
    print("Por favor, introduce un valor númerico")

    edad= input("Introduce la edad: ")

if (int(edad)<18):
    print("No puede pasar")
else:
    print("Puedes pasar")