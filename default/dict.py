# DICTIONARY
info={
    "nome":"Kalebe", # --> dict
    "idade":18
}
# muito parecido com JSON

print("Nome: " + info["nome"], " , " , "Idade: ", info["idade"]) 

for x,y in info.items():
    print(x, ":", y)
# imprmindo chave e valores