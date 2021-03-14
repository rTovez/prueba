from tkinter import * #
root = Tk() #crear raíz (caja)
root.geometry("600x450")
root.config(bg="blue")
frame = Frame(root, width=500, height=400, bg="Yellow")
frame.pack()
hora_inicio = 9
hora_final = 10
hora_ingreso = 9.5
numero_estudiante = 0 # cero estudiantes en la sala virtual
en_clase = False # estudiante esta o no en la sala virtual
estado_actual = IntVar()
encabezado = Label(frame, text="SALA VIRTUAL", font=("Arial Bold", 20), fg="blue")
encabezado.place(x=150, y=10)
Label(frame, text="Nombre: ").place(x=100, y=100)
nuevo_estudiante = Entry(frame, bd=2)
nuevo_estudiante.place(x=180, y=100)
   
def cambiarEstado():
    opcion_seleccionada = estado_actual.get()
    if opcion_seleccionada == 1:
        Label(frame, text="está en clase").place(x=280, y=200)
    elif opcion_seleccionada == 2:
        Label(frame, text="está en sala de espera").place(x=280, y=200)
    else:
        Label(frame, text="está ausente").place(x=280, y=200)    
        
def agregarAsistente():
    nombre = nuevo_estudiante.get()
    nuevo_asistente = Label(frame, text=nombre)
    nuevo_asistente.place(x=200, y=200)
    nuevo_estudiante.delete(0, END)
    
    estado_en_clase = Radiobutton(frame, text="En clase", variable=estado_actual, value=1, command=cambiarEstado)
    estado_en_clase.place(x=200, y=240)
    estado_en_espera = Radiobutton(frame, text="En espera", variable=estado_actual, value=2, command=cambiarEstado)
    estado_en_espera.place(x=200, y=270)
    estado_ausente = Radiobutton(frame, text="Ausente", variable=estado_actual, value=3, command=cambiarEstado)
    estado_ausente.place(x=200, y=300)
 
#agregar_asistente() #ejecutando la función    
boton_agregar = Button(frame, text="Unirse ahora", command=agregarAsistente)
boton_agregar.place(x=330, y=100)
root.mainloop()