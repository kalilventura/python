noite = False
msg = "Agora é noite" if noite else "Agora é dia"
print(msg)


idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Digite apenas números')
else:
    idade = int(idade)
    maior_idade = (idade >= 18)
    msg = 'Maior de idade' if maior_idade else 'Não é maior de idade.'

    print(msg)
