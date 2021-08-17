class Cliente:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} foi apagado')


class Endereco:
    def __init__(self, cidade, estado) -> None:
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade} foi apagado')


cli = Cliente('kalil')
cli.inserir_endereco('Jandira', 'São Paulo')
print(cli.nome)
cli.listar_enderecos()
del cli
