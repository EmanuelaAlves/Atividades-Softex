class Sanduíche:
    def getDescricao(self):
        return "Sanduíche"

    def getCusto(self):
        return 0


class FrangoAssado(Sanduíche):
    def __init__(self):
        self._custo = 4.50

    def getDescricao(self):
        return "Frango Assado"


class Pepperoni(Sanduíche):
    def __init__(self, sanduíche):
        self._sanduíche = sanduíche
        self._custo = 0.99

    def getDescricao(self):
        return self._sanduíche.getDescricao() + ", Pepperoni"

    def getCusto(self):
        return self._sanduíche.getCusto() + self._custo


class QueijoMussarelaRalado(Sanduíche):
    def __init__(self, sanduíche):
        self._sanduíche = sanduíche
        self._custo = 2.00

    def getDescricao(self):
        return self._sanduíche.getDescricao() + ", Queijo Mussarela Ralado"

    def getCusto(self):
        return self._sanduíche.getCusto() + self._custo


sanduíche = QueijoMussarelaRalado(Pepperoni(FrangoAssado()))

print("{} custa ${:.2f}.".format(sanduíche.getDescricao(), sanduíche.getCusto()))