from tkinter import *

def imprimirEsporte():
    print(vesporte.get())

app=Tk()
app.title("Teste de tkinter")
app.geometry("500x400")
app.configure(background="#dde")

listaEsportes=["Futebol", "Volei", "Basquete"]

vesporte=StringVar()
vesporte.set(listaEsportes[0])

bl_esportes=Label(app,text="Esportes")
bl_esportes.pack()

# RADIO BUTTON
#rb_futebol=Radiobutton(app,text="Futebol",value="f",variable=vesporte)   
#rb_futebol.pack()

#rb_volei=Radiobutton(app,text="Volei",value="v",variable=vesporte)
#rb_volei.pack()

#rb_basquete=Radiobutton(app,text="Basquete",value="b",variable=vesporte)
#rb_basquete.pack()


# OPTION MENU
op_esportes=OptionMenu(app,vesporte,*listaEsportes)                   
op_esportes.pack()

btn_esporte=Button(app,text="Escolher",command=imprimirEsporte)
btn_esporte.pack()

app.mainloop()