from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, num1, num2):
        pass

class Soma(Strategy):
    def execute(self, num1, num2):
        return num1 + num2

class Subtracao(Strategy):
    def execute(self, num1, num2):
        return num1 - num2

class Multiplicacao(Strategy):
    def execute(self, num1, num2):
        return num1 * num2

class Calculadora:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calcular(self, num1, num2):
        return self.strategy.execute(num1, num2)

if __name__ == '__main__':
    calculadora = Calculadora()

    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    operacao = input('Digite a operação desejada (+ para soma, - para subtração, * para multiplicação): ')

    if operacao == '+':
        calculadora.set_strategy(Soma())
    elif operacao == '-':
        calculadora.set_strategy(Subtracao())
    elif operacao == '*':
        calculadora.set_strategy(Multiplicacao())

    resultado = calculadora.calcular(num1, num2)
    print('Resultado:', resultado)