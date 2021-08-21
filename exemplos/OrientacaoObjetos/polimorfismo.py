"""
Polimorfismo é o principio que permite que classes derivadas de uma mesma superclasse tenham metodos iguais (de mesma assinatura)
mas comportamentos diferentes.
Mesma assinatura = Mesma quantidade e tipo de parametros

Obs: O Python só suporta esse tipo de polimorfismo(sobreposicao)
"""
from abc import ABC, abstractclassmethod


class A(ABC):
    @abstractclassmethod
    def falar(self, msg): pass


class B(A):
    def falar(self, msg):
        print(f'B está falando {msg}')


class C(B):
    def falar(self, msg):
        print(f'C está falando {msg}')


b = B()
c = C()
b.falar('Banana')
c.falar('Abacaxi')