from tkinter import *

app=Tk()
app.title("Teste de tkinter")
app.geometry("500x400")
app.configure(background="#dde")

# SPIN BOX - BARRA DE SELECAO
sb_valores=Spinbox(app,from_=0,to=100) #values=10,20,30,40,50,60,70,80,90,100
sb_valores.pack()

btn_valores=Button(app,text="Escolher",command=lambda:print(sb_valores.get()))          
btn_valores.pack()

app.mainloop()