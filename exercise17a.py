# crea un programa que pida números infinitamente. Los números introducidos deben 
# ser cada vez mayores El programa finalizará cuando se introduce un número menor que 
# el anterior.

num1 = int(input("Introduzca un número: "))
num2 = int(input("introduce un numero mayor que " +str(num1) + ": "))

while num2>num1:
    num1=num2
    num2= int(input("introduce un numero mayor que " +str(num1) + ": "))

print()
print(str(num2), "no es mayor que", str(num1))
