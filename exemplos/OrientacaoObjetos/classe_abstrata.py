from abc import ABC, abstractclassmethod

# Classes com o decorator abstractclassmethod não podem ser instanciadas, caso for tentado, vai ser executado um erro


class A(ABC):
    @abstractclassmethod
    def falar(self):
        pass


class B(A):
    def falar(self):
        print('Falando em B')


b = B()
b.falar()
