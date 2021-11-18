from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar

# cuadroTexto.place(x=100, y=100) # grid crea una tabla para divir de una mejor manera la interfaza
# así podemos colocar los objetos o textos alineados de manera correcta
cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, padx=10, pady=10)

scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

# El pad me permitira dar margenes o espacios entre objetos en los ejes x y y
# nombreLabel.place(x=100,y=100)
nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Dirección:")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

def codigoBoton():

    minombre.set("Juan")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)

botonEnvio.pack()

# alinear a la izquierda, abajo, derecha, arriba
# se hace con sticky

raiz.mainloop()