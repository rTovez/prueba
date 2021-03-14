from tkinter import*
ventana = Tk()
frame = Frame(ventana, width=500, height=400)
frame.pack()

hora_inicio= 9
hora_final = 10
hora_ingreso = 9.5
en_clase= False
n=0
l=0
for x in range(0,6,1):
    n=n+1
    l=l + 0
    if hora_ingreso >=hora_inicio and hora_ingreso< hora_final and en_clase== False:
        en_clase = True
        if n == 1:
            N1=1
        elif n == 2:
            N1=2
        elif  n == 3:
            N1=3
        elif  n == 4:
            N1=4
        elif  n == 5:
            N1=5
        elif  n == 6:  
            N1=6
        en_clase= False     
        asistente = Label(frame, text="asistente"+str(N1))
        asistente.place(x=100, y=l)
    else:
        N1="La clase ya terminó"
        asistente = Label(frame, text=N1)
        asistente.place(x=100, y=200)
        break
    
    
ventana.mainloop()    


