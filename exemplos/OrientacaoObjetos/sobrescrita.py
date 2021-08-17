class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'{self.nome} está falando ...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} está comprando ...')

    def falar(self):
        print(f'Cliente {self.nome} está falando ...')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome) -> None:
        super().__init__(nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        # Para escolher qual classe eu quero utilizar a sobrescrita, é só chamar o classe.metodo(self)
        super().falar()
        print(f'{self.nome} é VIP e está falando ...')
