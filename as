
for fila in range (100,300,100):
    for columna in range (100, 400, 100):
        numero_estudiate = numero_estudiate + 1
        if hora_ingreso >= hora_inicio and hora_ingreso < hora_final and en_clase == False:
            asistente= Label(frame, text="Estudiante" +str(numero_estudiate))
        asistente. place(x=columna, y=fila)

nombre= Label(frame, text= "Nombre: ")
nombre.place(x=100, y=300)
nuevo_estudiante= Entry(frame, bd=2)
nuevo_estudiante.place(x=180, y=300)

def agregar_asistente(): 
    nuevo_asistente= Label (frame, text="asistente agregado")
    nuevo_asistente.place(x=190, y=330)

boton_agregar= Button(frame, text="Unirse ahora", command=agregar_asistente)
boton_agregar.place(x=340, y=300)
        
root.mainloop()

