from math import sqrt


class EquacaoDoSegundoGrau:
    def __init__(self, coeficiente_a, coeficiente_b, coeficiente_c):
        self.delta = 0
        self.primeiraraiz = 0
        self.segundaraiz = 0
        self.coeficiente_a = coeficiente_a
        self.coeficiente_b = coeficiente_b
        self.coeficiente_c = coeficiente_c

    def discriminante(self):

        self.delta = self.coeficiente_b * self.coeficiente_b - 4 * self.coeficiente_a * self.coeficiente_c
        return print(f'O valor do discriminante da equação é {self.delta}')

    def raizes(self, delta):

        if self.delta > 0:
            self.primeiraraiz = (-self.coeficiente_b + sqrt(self.delta)) / (2 * self.coeficiente_a)
            self.segundaraiz = (-self.coeficiente_b - sqrt(self.delta)) / (2 * self.coeficiente_a)

            return print(f'As raizes da equação são {self.primeiraraiz} e {self.segundaraiz}')

        elif self.delta == 0:
            primeiraraiz = (-self.coeficiente_b + sqrt(self.delta)) / (2 * self.coeficiente_a)

            return print(f'As raizes da equação são {self.primeiraraiz} e {self.segundaraiz}')

        else:
            return print(f'O discriminante é negativo, a equação não possui raíz')


coeficiente_a = float(input("Digite o coeficiente a = "))
coeficiente_b = float(input("Digite o coeficiente b = "))
coeficiente_c = float(input("Digite o coeficiente b = "))

equacao = EquacaoDoSegundoGrau(coeficiente_a, coeficiente_b, coeficiente_c)

print(f'A equação é ({equacao.coeficiente_a})x² + ({equacao.coeficiente_b})x + ({equacao.coeficiente_c}) = 0')
equacao.raizes(equacao.discriminante())
