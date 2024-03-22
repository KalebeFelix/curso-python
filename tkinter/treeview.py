from tkinter import *
from tkinter import ttk

app=Tk()
app.title("Teste de tkinter")
app.geometry("500x400")
app.configure(background="#dde")

listaNomes=[["0","kalebe","85988898800"],["1","herisberto","85987965432"]]

# TREEVIEW - TABELA DE DADOS
tv=ttk.Treeview(app,columns=("id","nome","fone"),show="headings")
tv.column("id",minwidth=0,width=50)
tv.column("nome",minwidth=0,width=250)
tv.column("fone",minwidth=0,width=100)                             
                                                                    
tv.heading("id",text="ID")
tv.heading("nome",text="Nome")
tv.heading("fone",text="Telefone")
tv.pack()

for i in listaNomes:
    tv.insert("","end",values=i)

app.mainloop()
