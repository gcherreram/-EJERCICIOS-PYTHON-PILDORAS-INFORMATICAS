# Tambien denominadas GUI (Graphic user Interface), son intermediarios entre el programa
# y el usuario
# Formadas por un conjunto de gráficvos como ventanas, botones, menus, casillas de verificación etc.
# Librerias con las que trabajar para crear un GUI
# Tkinter
# WxPython
# PyQT
# PyGTK
#Tkinter es un "puente" entre python y lla libreria TCL/TK
# Lo primero que tenemos que construir es la raiz (esto se conoce com la ventana)
# Luego sigue un frame dentro de esa ventana con widgets

from tkinter import *

raiz=Tk()

raiz.title("Mi primera ventana")

raiz.resizable(1,1) #Primer número width ancho, segundo height alto
# 0 es false y 1 es true, o sea pueden usar false y true.

raiz.iconbitmap("gato.ico")
# Se debio colocar el r para que lea la ruta en crudo, ya que no reconocia
# del modo raiz.iconbitmap("gato.ico")

#raiz.geometry("650x350")
# Con esto se cambia el tamaño de la gráfica

raiz.config(bg="blue")
# Aquí con bg(background) se cambia el fondo 

miFrame=Frame()

# Se debe empacar el frame en la raiz
miFrame.pack() #(fill="both", expand="true")

miFrame.config(bg="red")

miFrame.config(width="650", height="350")

miFrame.config(bd=35)

# Configurar el borde
miFrame.config(relief="sunken")

#cambiar el cursor
miFrame.config(cursor="hand2")

raiz.mainloop()


