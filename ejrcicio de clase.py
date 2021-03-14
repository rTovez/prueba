from tkinter import *

root= Tk()
root.geometry("600x450")
root.config(bg="blue")
frame= Frame(root, width=500, height=400, bg="yellow")
frame.pack()
hora_inicio= 9
hora_final= 10
hora_ingreso= 9.5
numero_estudiate= 0
en_clase= False
estado_actual= IntVar()
encabezado= Label(frame, text="S A L A  V I R T U A L", font=("Arial Bold", 20),fg="blue")
encabezado.place(x=150, y=10)
Label(frame, text="Nombre: ").place(x=100,y=100)
nuevo_estudiante= Entry(frame, bd=2)
nuevo_estudiante.place(x=180, y=100)

def cambiarEstado():
    opcion_seleccionada = estado_actual.get()
    if opcion_seleccionada == 1:
        Label(frame, text="esta en clase",fg="green").place(x=280, y=200)
    elif opcion_seleccionada == 2:
        Label(frame, text="esta en sala de espera",fg="yellow").place(x=280, y=200)
    else:
        Label(frame, text="esta ausente",fg="red",).place(x=280, y=200)

def agregarAsistente():
    nombre = nuevo_estudiante.get()
    nuevo_asistente= Label(frame, text=nombre)
    nuevo_asistente.place(x=200, y=200)
    nuevo_estudiante.delete(0,END)

    estado_en_clase= Radiobutton(frame, text="En Clase", variable=estado_actual, value=1, command=cambiarEstado)
    estado_en_clase.place(x=200, y=240)
    estado_en_clase= Radiobutton(frame, text="En espera", variable=estado_actual, value=2, command=cambiarEstado)
    estado_en_clase.place(x=200, y=270)
    estado_en_clase= Radiobutton(frame, text="Ausente", variable=estado_actual, value=3, command=cambiarEstado)
    estado_en_clase.place(x=200, y=300)

boton_agregar= Button(frame, text="Unirse Ahora", command=agregarAsistente)
boton_agregar.place(x=330, y=100)

root.mainloop()
 
