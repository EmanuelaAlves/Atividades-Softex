import pickle

class Endereco:
    def __init__(self, rua, numero, cidade, estado):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado

endereco = Endereco ("Bonita", 123, "Paraiso", "Bahia")

with open('endereco.pickle', 'wb') as f:
    pickle.dump(endereco, f)

with open('endereco.pickle', 'rb') as f:
    endereco_serializado = pickle.load(f)

print("Rua:", endereco_serializado.rua)
print("Número:", endereco_serializado.numero)
print("Cidade:", endereco_serializado.cidade)
print("Estado:", endereco_serializado.estado)

