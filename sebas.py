nombre = input("Ingrese su nombre: ")
contar = len(nombre)

while (contar >= 6 and contar <= 12):
    if contar < 6:
        print("nombre menor a 6")
        nombre = input("Ingrese su nombre: ")
    if contar < 6:
        print("nombre mayor a 12")
        nombre = input("Ingrese su nombre: ")

print("Nombre valido")
