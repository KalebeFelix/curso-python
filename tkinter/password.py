from tkinter import *

app=Tk()
app.title("Teste de tkinter")
app.geometry("500x400")
app.configure(background="#dde")

vsenha=StringVar()

#senha password (show="*")
Label(app,text="Escreva uma senha").pack()                           
p_senha=Entry(app,show="*",textvariable=vsenha)
p_senha.pack()

btn_senha=Button(app,text="Enviar",command=lambda:print(vsenha.get()))
btn_senha.pack()

app.mainloop()