from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, modelo, marca, cor, numeroRodas):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.numeroRodas = numeroRodas

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def represent(self):
        pass


class Carro(Veiculo):
    def __init__(self, modelo, marca, cor, numeroRodas, numeroPortas):
        super().__init__(modelo, marca, cor, numeroRodas)
        self.numeroPortas = numeroPortas

    def clone(self):
        return Carro(self.modelo, self.marca, self.cor, self.numeroRodas, self.numeroPortas)

    def represent(self):
        return f"Carro {self.modelo} {self.marca}, cor {self.cor}, {self.numeroRodas} rodas, {self.numeroPortas} portas."


class Moto(Veiculo):
    def __init__(self, modelo, marca, cor, numeroRodas, tipo):
        super().__init__(modelo, marca, cor, numeroRodas)
        self.tipo = tipo

    def clone(self):
        return Moto(self.modelo, self.marca, self.cor, self.numeroRodas, self.tipo)

    def represent(self):
        return f"Moto {self.modelo} {self.marca}, cor {self.cor}, {self.numeroRodas} rodas, {self.tipo} tipo."


class Aplicacao:
    
    def __init__(self):
        self.veiculos = [
            Carro("Gol", "Volkswagen", "preto", 4, 4),
            Carro("Palio", "Fiat", "vermelho", 4, 2),
            Moto("CB 300", "Honda", "amarela", 2, 300),
            Moto("Fazer", "Yamaha", "azul", 2, 250),
            Carro("Corolla", "Toyota", "prata", 4, 4),
            Moto("pop", "Honda", "vermelha", 2, 100)
        ]

    def clone_veiculos(self):
        clones = []
        for veiculo in self.veiculos:
            clones.append(veiculo.clone())
        return clones


if __name__ == "__main__":
    app = Aplicacao()
    clones = app.clone_veiculos()
    for clone in clones:
        print(clone.represent())