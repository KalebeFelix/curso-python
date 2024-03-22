from tkinter import *
from tkinter import ttk

app=Tk()
app.title("Teste de tkinter")
app.geometry("500x400")
app.configure(background="#dde")

listaEsportes=["Futebol","Volei","Basquete"]

Label(app,text="Escolha um tipo de Esporte").pack()             

# COMBO BOX
cb_esporte=ttk.Combobox(app,values=listaEsportes)
cb_esporte.set("Selecione")
cb_esporte.pack()

btn_esporte=Button(app,text="Escolher",command=lambda:print(cb_esporte.get()))
btn_esporte.pack()

app.mainloop()