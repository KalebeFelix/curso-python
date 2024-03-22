import json 

#arquivo json
info_json = '{"nome": "kalebe", "idade": 17}' 

# converte em dicionario
info = json.loads(info_json)
for i,n in info.items():
    print(f'{i}: {n}')



info_list = ['kalebe', 'hadassah', 'clayton']

# converte em json
info_j = json.dumps(info_list)    