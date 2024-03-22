from tkinter import *
def dados():
    print("Nome: ",nome.get())
    print("Telefone: ",tel.get())
    print("E-mail: ",email.get())
    print("OBS: ",obs.get("1.0",END))

app=Tk()
app.title("Teste de tkinter")
app.geometry("500x400")
app.configure(background="#dde")

# adcionando conteudo
txt1=Label(app,text="Teste",fg="black",bg="yellow")    
txt1.place(x=10,y=10,width=100,height=20)

Label(app,text="Nome",fg="black",bg="#dde",anchor="w").place(x=10,y=50,width=100,height=20)
# entrada / input
nome=Entry(app)                                      
nome.place(x=10,y=70,width=100,height=20)

Label(app,text="Telefone",fg="black",bg="#dde",anchor="w").place(x=10,y=100,width=100,height=20)
tel=Entry(app)
tel.place(x=10,y=120,width=100,height=20)

Label(app,text="E-mail",fg="black",bg="#dde",anchor="w").place(x=10,y=150,width=100,height=20)
email=Entry(app)
email.place(x=10,y=170,width=100,height=20)

Label(app,text="OBS",fg="black",bg="#dde",anchor="w").place(x=10,y=200,width=100,height=20)

#entrada com mais de uma linha 
obs=Text(app)                                          
obs.place(x=10,y=220,width=200,height=70)

Button(app,text="Enviar",command=dados).place(x=10,y=300,width=100,height=20)
 

#--> roda o programa
app.mainloop()                                          