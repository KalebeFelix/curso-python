from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# FORMULARIO USANDO TREEVIEW

def inserir():
    if vid.get() == "" or vnome.get() == "" or vefone.get() == "":
        messagebox.showerror("Error","Preencha todos os campos")
    else:
        tv.insert("","end",values=(vid.get(),vnome.get(),vefone.get()))
        vid.delete(0,END)
        vnome.delete(0,END)
        vefone.delete(0,END)
        vid.focus()  

def deletar():
    try:
        inteSelecionado=tv.selection()[0]
        tv.delete(inteSelecionado)
    except:
        messagebox.showerror("Error","Selecione um contato")

def Obter():
    try:
        inteSelecionado=tv.selection()[0]
        valores=tv.item(inteSelecionado,"values")
        print("ID.......:"+valores[0])
        print("Nome.....:"+valores[1])
        print("Telefone.:"+valores[2])
    except:
        messagebox.showerror("Error","Selecione um contato")

app=Tk()
app.title("Teste de tkinter")
app.geometry("500x400")
app.configure(background="#dde")

lbid=Label(app,text="ID")
vid=Entry(app)

lbnome=Label(app,text="Nome")                                
vnome=Entry(app)

lbfone=Label(app,text="Telefone")
vefone=Entry(app)


tv=ttk.Treeview(app,columns=("id","nome","fone"),show="headings")
tv.column("id",minwidth=0,width=50)
tv.column("nome",minwidth=0,width=250)
tv.column("fone",minwidth=0,width=100)                          
                                                                    
tv.heading("id",text="ID")
tv.heading("nome",text="Nome")
tv.heading("fone",text="Telefone")

btn_inserir=Button(app,text="Inserir",command=inserir)
btn_deletar=Button(app,text="Deletar",command=deletar)
btn_obter=Button(app,text="Obter",command=Obter)

lbid.grid(column=0,row=0,sticky="w")
vid.grid(column=0,row=1)

lbnome.grid(column=1,row=0,sticky="w")
vnome.grid(column=1,row=1)

lbfone.grid(column=2,row=0,sticky="w")
vefone.grid(column=2,row=1)

tv.grid(column=0,row=2,columnspan=3,pady=5)

btn_inserir.grid(column=0,row=3)
btn_deletar.grid(column=1,row=3)
btn_obter.grid(column=2,row=3)

app.mainloop()