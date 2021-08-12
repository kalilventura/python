nome = 'Kalil'
idade = 23
altura = 1.70
maior_idade = idade > 18
peso = 90
imc = peso / (altura **2)

## Formatando string
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')

#Outras maneiras
# '{0} tem {1} anos de idade e seu imc é {2}'.format(nome, idade, imc)
# '{n} tem {i} anos de idade e seu imc é {im}'.format(n=nome, i=idade, im=imc)
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))