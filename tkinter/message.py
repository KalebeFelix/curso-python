from tkinter import *
from tkinter import messagebox

# TIPOS DE MENSAGENS
def mostrarMsg(tipo,msg):
    if tipo=="info":                                           
        messagebox.showinfo("Informação",msg)
    elif tipo=="warning":
        messagebox.showwarning("Atenção",msg)
    elif tipo=="error":
        messagebox.showerror("Erro",msg)


app=Tk()
app.title("Teste de tkinter")
app.geometry("500x400")
app.configure(background="#dde")

listaMsg=["info", "warning","error"]
vnum=StringVar()
vnum.set(listaMsg[0])

Label(app,text="Escolha um tipo de MessageBox").pack()
op_menu=OptionMenu(app,vnum,*listaMsg)
op_menu.pack()

Label(app,text="Escreva uma mensagem").pack()
vmsg=Entry(app)
vmsg.pack()

btn=Button(app,text="Enviar",command=lambda:mostrarMsg(vnum.get(),vmsg.get()))
btn.pack()



app.mainloop()