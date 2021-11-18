# Crea un programa que pida números positivos indefinidamente. El programa termina 
# cuando se introduce un número negativo. Finalmente el programa muestras la suma de 
# todos los números introducidos

operador = 0
num = int(input("Por favor introduzca un número: "))

while num>0:
    operador = operador + num
    num = int(input("Por favor introduzca otro número: "))

print("Ha ingresado un númerp invalido, la suma de los números que ingreso es: " + str(operador))
