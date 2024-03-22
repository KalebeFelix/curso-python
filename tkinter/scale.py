from tkinter import *
app=Tk()
app.title("Teste de tkinter")
app.geometry("500x400")
app.configure(background="#dde")

# SCALE - BARRA DE ESCALA
Label(app,text="Valor").pack()
scale=Scale(app,from_=0,to=100,orient=HORIZONTAL)                   
scale.set(50)
scale.pack()

app.mainloop()