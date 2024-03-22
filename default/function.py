# FUNCTIONS
def somar(n1,n2):
    res=n1+n2
    print("O resultado e:", res)  

somar(5,3)


#funcao com parametros infinitos(arbitrário)*
def add(*n):
    r=0
    for i in n:              
        r+=i
    print("soma:", r)

add(1,2,3,4,5) 

#funcao lambda/anonima
facil = lambda x,y: x+y
print(facil(2,5))           