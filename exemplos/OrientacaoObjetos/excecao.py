class TesteError(Exception):
    pass


def testar():
    raise TesteError('Deu um erro')


try:
    testar()
except TesteError as error:
    print(f'{error}')
