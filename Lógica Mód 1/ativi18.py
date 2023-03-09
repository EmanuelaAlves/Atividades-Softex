class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, n):
        return ComplexNumber(self.real + n.real, self.imag + n.imag)

    def __sub__(self, n):
        return ComplexNumber(self.real - n.real, self.imag - n.imag)

    def __mul__(self, n):
        return ComplexNumber(self.real * n.real - self.imag * n.imag, self.real * n.imag + self.imag* n.real)

    def __truediv__(self, n):
        denominator = n.real ** 2 + n.imag ** 2
        return ComplexNumber((self.real * n.real + self.imag * n.imag) / denominator, (self.imag * n.real - self.real * n.imag) / denominator)

    def __str__(self):
        if self.imag< 0:
            return f"{self.real} - {-self.imag}i"
        else:
            return f"{self.real} + {self.imag}i"


# Cálculo de três números complexos
a = ComplexNumber(2, 3)
b = ComplexNumber(-1, 2)
c = ComplexNumber(0, -1)

# Realizando todas as operações básicas
soma = a + b
subtracao = a - b
multiplicacao = a * c
divisao = a / b

# Imprimindo as propriedades real e imaginária do número
print(f"A parte real do número a é {a.real}")
print(f"A parte imaginária do número a é {a.imag}")
