class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'{self.nome} está falando ...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} está comprando ...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} está estudando ...')


p = Cliente('Kalil', 23)
print(p.nome)
p.falar()
p.comprar()

a = Aluno('Joao', 44)
print(a.nome)
a.falar()
a.estudar()
