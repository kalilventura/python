def primeira_funcao():
    return "Hello World"


print(primeira_funcao())


def saudacao(nome, mensagem):
    return '{nome}, {mensagem}'.format(nome=nome, mensagem=mensagem)


"""
    Argumentos em funçoes:
    *args -> Usamos quando não sabemos quantos argumentos serão passados para função
    **kwargs -> key word arguments (argumentos com palavras chaves, ou seja, argumentos com nomes)
"""


def func(*args, **kwargs):
    print(args)
    print(kwargs)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
func(*lista, 9, 'O * antes da lista significa que desestruturei a lista',
     nome='Kalil', sobrenome='Ventura')


"""
    Palavra reservada global
    Quando queremos alterar uma variavel global em uma funcao
"""
nome = 'Jose'
print(nome)


def altera_var():
    global nome
    nome = 'Kalil'
    print(nome)


print(nome)
