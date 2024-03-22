# CLASSE

class carrros: 
    velMax=0             
    cor = ''

    #init inicializa junto com a classe
    def __init__(self,v,c):   
        self.velMax=v
        self.cor=c

    def mostrar(self):
        print('Velocidade maxima:', self.velMax,  '\nCor:', self.cor)

c1=carrros(150,'azul')
c1.mostrar()



#classe pai, super classe
class NPC:   
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vida=True
        self.energia=100
    def info(self):
        print("Nome:", self.nome)
        print("Time:", self.time)
        print("Forca:", self.forca)
        print("Municao:", self.municao)
        print("Vida:", ("sim" if self.vida else "nao"))
        print("Energia:", self.energia)
    
#classe filha
class soldado(NPC):  
    def __init__(self,nome,time):
        self.forca=200
        self.municao=50

        #--> acessa a classe pai
        super().__init__(nome, time, self.forca, self.municao)   

s1=soldado("kalebe", "brasil")

s1.vida=False

# chamando a função que esta dentro da classe
s1.info()



# Criando uma lista de objetos
lista = []

class info:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

def adc():
    nome=input("Digite seu nome:")
    idade=input("Digite sua idade:")
    lista.append(info(nome, idade))

adc()