from tkinter import *

app=Tk()
app.title("Teste de tkinter")
app.geometry("500x400")
app.configure(background="#dde")

listaEsportes=["Futebol","Volei","Basquete"]

# LIST BOX
lb_esporte=Listbox(app)                                           
for e in listaEsportes:
    lb_esporte.insert(END,e)
lb_esporte.pack()

vesporte=Entry(app)
vesporte.pack()
btn_adc=Button(app,text="Adcionar Novo Esporte",command=lambda:lb_esporte.insert(END,vesporte.get()))
btn_adc.pack()

btn_esporte=Button(app,text="Escolher",command=lambda:print(lb_esporte.get(ACTIVE)))
btn_esporte.pack()

app.mainloop()