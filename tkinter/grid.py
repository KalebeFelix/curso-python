from tkinter import *

app=Tk()
app.title("Teste de tkinter")
app.geometry("500x400")
app.configure(background="#dde")

lb_info=Label(app,text="Informações")
lb_nome=Label(app,text="Nome")
lb_idade=Label(app,text="Idade")

et_nome=Entry(app)                                      
et_idade=Entry(app)

btn=Button(app,text="Adcionar",command=lambda:print(et_nome.get(),et_idade.get()))

# GRID
lb_info.grid(column=0,row=0,pady=5)      #sticky n=cima , s=baixo , e=direita , w=esquerda
lb_nome.grid(column=0,row=1,sticky="w")  #columnspan mescla colunas
et_nome.grid(column=0,row=2)
lb_idade.grid(column=0,row=3,sticky="w")
et_idade.grid(column=0,row=4)
btn.grid(column=0,row=5,pady=5)

app.mainloop()