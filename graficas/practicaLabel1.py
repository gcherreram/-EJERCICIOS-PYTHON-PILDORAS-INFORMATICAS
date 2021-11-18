from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

miImagen=PhotoImage(file="raton.png")
miImagen.config(siz)

Label(miFrame, image=miImagen).place(x=100, y=200)
# Label(miFrame, text = "Hola alumnos de python", fg= "red", font=("Comic Sans MS", 18)).place(x=100, y=200)
# miLabel.pack

root.mainloop()
