class Empresa:
    def __init__(self, nome, cnpj, endereco):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
    
    def __str__(self):
        return f"{self.nome} - CNPJ: {self.cnpj} - Endereço: {self.endereco}"
    