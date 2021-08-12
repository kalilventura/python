"""
    append -> Adiciona um dado na lista no final
    insert -> Adiciona um dado antes do indice
    pop -> Remove o ultimo dado da lista
    extend -> Extende a lista
    + -> junta listas
"""

lista = []
lista.append('a')
lista.insert(0, 'b')
print(lista)

lista.pop()
lista
print(lista)

frutas = ['Maca', 'Banana', 'Abacaxi', 'Tomate', 'Caju']
verduras = ['Alface', 'Cenoura', 'Batata']

frutas_vegetais = frutas + verduras
print(frutas_vegetais)

e = ['q']
f = ['p']
e.extend(f)

print(e)

# Desestruturacao da lista
n1, n2, n3 = verduras
print(n1, n2, n3)