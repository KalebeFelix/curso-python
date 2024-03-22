nome="clayton kalebe"  
res= "kalebe" in nome  
# Verifica se kalebe esta dentro da string, pode usar um upper() em ambos: para nao diferenciar maiusculas e minusculas.  
# Retorna um boolean


#--------------------------------------------------------------------------------------------------

# Formatação de strings
cidade = "sao paulo"
dia = "sabado"
mes = "dezembro"
ano = 2023                     

data1 = "{}, {} de {} de {}".format(cidade, dia, mes, ano) 
#concatena tudo na mesma variavel, usando .format 

print(data1.upper())
# Retorna tudo em maiusculas 

# F-strings
cidade = "sao paulo"
dia = "sabado"
mes = "dezembro"
ano = 2023                     

data = f"{cidade}, {dia} de {mes} de {ano}"

print(data.upper())
