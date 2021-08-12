# Entrada de dados

nome = input("Qual seu nome?")
idade = input('Qual sua idade?')

ano_nascimento = 2021 - int(idade)

print(f'usuario digitou {nome} e o tipo da variavel eh {type(input)}')

print(f'{nome} tem {idade} anos.')
print('Ano de nascimento {}'.format(ano_nascimento))