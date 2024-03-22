from tkinter import *
from tkinter import messagebox

def mostrar(vmsg):
    messagebox.showinfo("Informação",vmsg.get())

app=Tk()
app.title("Teste de tkinter")
app.geometry("500x400")
app.configure(background="#dde")

# FRAME (QUADRO/CONTAINER)
fr=Frame(app,borderwidth=1, relief="sunken")         
fr.place(x=10,y=10,width=250,height=80)

Label(fr,text="Escreva uma mensagem").pack()
vmsg=Entry(fr)
vmsg.pack()

btn=Button(fr,text="Enviar",command=lambda:mostrar(vmsg))
btn.pack()

app.mainloop()