import copy
"""
    Como declarar e utilizar dicionarios
"""

# Declarar
dicionario = {"chave": "valor"}
dicionario1 = dict(chave='valor', chave1='valor1')

# Acessar
print(dicionario["chave"])
print(dicionario1["chave1"])

# Copiar os valores para outra variavel
dic = {1: 'a', 2: 'b', 3: 'c', 'd': ['Kalil', 'Ventura']}

# Shallow Copy (Conseguimos alterar elementos mais internos do dicionario, caso seja um complexo)
# v = dic.copy()
# Deep Copy
v = copy.deepcopy(dic)


v[1] = 'Lala'
v['d'][0] = 'Joao da Silva'

print(dic)
print(v)
