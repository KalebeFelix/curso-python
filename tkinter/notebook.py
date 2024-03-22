from tkinter import *
from tkinter import ttk

app=Tk()
app.title("Teste de tkinter")
app.geometry("500x400")
app.configure(background="#dde")

# NOTEBOOK - ABAS
nb=ttk.Notebook(app)
nb.place(x=0,y=0,width=500,height=400)

tb1=Frame(nb)
tb2=Frame(nb)                                            

nb.add(tb1,text="Apresentação")
nb.add(tb2,text="Contatos")

Label(tb1,text="Ola meu nome e Clayton Kalebe").pack()

Label(tb2,text="Telefone:8598888888 \n Email: example@example.com").pack()

app.mainloop()