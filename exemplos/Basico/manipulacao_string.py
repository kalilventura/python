texto = 'Hello World'

# Caso eu queira um caractere da string, ele e dividido por indices, entao, colocando o indice conseguimos buscar os dados com os indices
print(texto[5])

# Para remover um caractere da string, onde fazemos o "fatiamento" da string
url = 'www.google.com/'
print(url[:-1])

# Podemos tambem pegar pedaços da string
novo_texto = texto[0:5]
print(novo_texto)

# Pegar o texto pulando de dois em dois
novo_texto = texto[0::2]
print(novo_texto)

# dividindo uma string
string = 'O Brasil é penta.'
lista = string.split(' ')
print(lista)

# Juntando string
string2 = ','.join(lista)
print(string2)
