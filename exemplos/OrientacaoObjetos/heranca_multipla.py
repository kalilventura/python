class A:
    def falar(self):
        print('Estou em A')


class B(A):
    def falar(self):
        print('Estou em B')


class C(A):
    def falar(self):
        print('Estou em C')


class D(B, C):
    """
    Quando temos heranca multipla, a ordem das classes que sao colocadas importam
    """
    pass


d = D()
# Se a classe B não tiver o método, vai procurar na classe C
d.falar()
