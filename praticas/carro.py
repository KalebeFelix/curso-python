import os 

carros = []

class Carro:
    ligado=False
    def __init__(self, nome, placa, ano):
        self.nome = nome
        self.placa = placa
        self.ano = ano
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def info(self):
        print("Nome do carro..:", self.nome)
        print("Placa do carro.:", self.placa)
        print("Ano do carro...:", self.ano)
        print("Ligado.........:", ("S" if self.ligado==True else "N"))

def menu():
    os.system('cls')
    print("--------MENU--------")
    print("1 - Cadastrar Carro")
    print("2 - Listar Carros")
    print("3 - Informacoes do Carro:")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Excluir Carro")
    print("7 - Sair")
    print("Quantidade de Carros:", len(carros))
    opc = input("Opcao: ")
    return int(opc) 

def cadastra_carro():
    os.system('cls')
    n = input("Nome do carro: ")
    p = input("Placa do carro: ")
    a = input("Ano do carro: ")
    car = Carro(n, p, a)
    carros.append(car)
    os.system('pause')

def lista_carros():
    os.system('cls')
    p=0
    for car in carros:
        print(p,"-",car.nome)
        p+=1
    os.system('pause')

def info_carro():
    os.system('cls')
    print("--------INFORMACOES--------")
    x = input("Digite a Placa do Carro: ")
    for i in carros:
            if i.placa == x:
                i.info()
                break
            else:
                print("Carro nao encontrado")
    os.system('pause')    

def ligar_carro():
    os.system('cls')
    print("--------LIGAR--------")
    x = input("Digite a Placa do Carro: ")
    for i in carros:
            if i.placa == x:
                i.ligar()
                print("Carro ligado")
                break
            else:
                print("Carro nao encontrado")
    os.system('pause')       

def desligar_carro():
    os.system('cls')
    print("--------DESLIGAR--------")
    x = input("Digite a Placa do Carro: ")
    for i in carros:
            if i.placa == x:
                i.desligar()
                print("Carro desligado")
                break
            else:
                print("Carro nao encontrado")
    os.system('pause')       

def excluir_carro():
    os.system('cls')
    print("--------EXCLUIR--------")
    x = input("Digite a Placa do Carro: ")
    for i in carros:
        if i.placa == x:
            del carros[carros.index(i)]
            print("Carro excluido")  
            break      
        else:
            print("Carro nao encontrado")
    os.system('pause')    

a = menu()

while a < 7:
    if a == 1:
        cadastra_carro()
    if a == 2:
        lista_carros()
    if a == 3:
        info_carro()
    if a == 4:
        ligar_carro()
    if a == 5:
        desligar_carro()
    if a == 6:
        excluir_carro()
    a = menu()