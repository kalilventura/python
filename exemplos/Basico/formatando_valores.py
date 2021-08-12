"""
    Formatando valores:
    
    :s -> Texto (string)
    :d -> Inteiro (int)
    :f -> Números de ponto flutuante (float)
    :.(NUMERO)f -> Quantidade de casas decimais (float)
    :(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)
    
    > -> Esquerda
    < -> Direita
    ^ -> Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print(f'{divisao:.2f}')

# Formatação a esquerda com zeros
num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0>10}')

# Formatação a direita com zeros

print(f'{num_1:0<10}')
print(f'{num_2:0<10}')

# Formatação com o valor centralizado

print(f'{num_1:0^10}')
print(f'{num_2:0^10}')

# Funcionam com qualquer caractere, nao somente com numeros
nome = 'John'
print('{nome:@>15}'.format(nome=nome))