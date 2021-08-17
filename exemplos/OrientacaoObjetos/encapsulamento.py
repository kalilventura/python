"""
_ -> Protected (na realidade podemos acessar, mas pela filosofia da linguagem, não é recomendado)
__ -> Private (_NOMECLASSE__nomeatributo)
"""


class BaseDeDados:
    def __init__(self) -> None:
        self.dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' is not self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def listar_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

    def apagar_clientes(self, id):
        del self.dados['clientes'][id]
