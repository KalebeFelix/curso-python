from tkinter import *

def clicado():
    if vf.get() == 1:
        print("Futebol")
    if vv.get() == 1:
        print("Volei")
    if vb.get() == 1:
        print("Basquete")


        

app=Tk()
app.title("Teste de tkinter")
app.geometry("500x400")
app.configure(background="#dde")

vf=IntVar()
vv=IntVar()
vb=IntVar()

# CHECK BUTTON
cb_futebol=Checkbutton(app,text="Futebol",variable=vf,onvalue=1,offvalue=0)
cb_futebol.pack()

cb_volei=Checkbutton(app,text="Volei",onvalue=1,offvalue=0,variable=vv)                 
cb_volei.pack()

cb_basquete=Checkbutton(app,text="Basquete",onvalue=1,offvalue=0,variable=vb)
cb_basquete.pack()

b_esporte=Button(app,text="Escolher",command=clicado)
b_esporte.pack()

app.mainloop()