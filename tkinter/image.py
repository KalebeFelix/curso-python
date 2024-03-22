from tkinter import *

# ADC uma imagem
app=Tk()
app.title("Teste de tkinter")
app.geometry("500x400")
app.configure(background="#dde")
            
Label(app,PhotoImage(file="logo.png")).pack()

app.mainloop()