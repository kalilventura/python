"""
No Python, o comportamento dos operadores é definido por metodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuario.
"""


class Retangulo:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __repr__(self) -> str:
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    def __add__(self, other: object):
        x = self.x + other.x
        y = self.y + other.y
        return Retangulo(x, y)

    def __lt__(self, other: object):
        a1 = self.get_area()
        a2 = other.get_area()

        return True if a1 > a2 else False

    def __eq__(self, other: object) -> bool:
        return True if self.x == other.x and self.y == other.y else False


r1 = Retangulo(10, 20)
r2 = Retangulo(20, 40)
r3 = r1 + r2
print(r3)
