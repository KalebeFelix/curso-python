# FOR
lista=["1", "2", "3", "4"]

# FOR percorre o array
for i in lista:
    print(i)             
    if i == "3":
        break 
# break interrompe o FOR 
    
# WHILE
i=0

# WHILE executa enquanto a condicao for verdadeira
while i<10:
    print(i)         
    i+=1
    if i==5:
        break 

# PRATICA
nomes=[]
nome=input("digite seu nome: ")

while nome != "stop":                 
  nomes.append(nome)
  nome=input("digite um novo nome: ")
# usando um array e while para fazer uma lista de nomes 

for x in nomes:
    print(x)
# imprimindo a lista de nomes