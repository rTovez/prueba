from tkinter import *

root= Tk()
frame= frame(root, widht=500, height=400)
frame.pack()

hora_inicio= 9
hora_final= 10
hora_ingreso= 9,5
nombre_estudiante= "asistente 1"
en_clase= True

while hora_ingreso>= hora_inicio and hora_ingreso < hora_final and en_clase== False:
    asistente= label(marco, text=nombre_estudiante)
    asistente.place(x=100, y=200)

    en_clase= True


root.mainloop()

