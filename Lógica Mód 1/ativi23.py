class Pessoa:
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        if idade >= 20:
            self._idade = idade
        else:
            self._idade = 0

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str):
        self._nome = nome

    def get_idade(self) -> int:
        return self._idade

    def set_idade(self, idade: int):
        if idade >= 20:
            self._idade = idade

pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 20)


print(pessoa1.get_nome(), pessoa1.get_idade())  # João 30
print(pessoa2.get_nome(), pessoa2.get_idade())  # Maria 10