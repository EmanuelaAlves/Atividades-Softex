import datetime
anoMinimo = 1922
anoMaximo = 2021

while True:
    try:
        nomeCompleto = input("Informe seu nome completo: ")
        anoNascimento = int(input("Informe o ano do seu nascimento entre 1922 e 2021): "))
        
        if anoNascimento < anoMinimo or anoNascimento > anoMaximo:
            raise valueError
            
        idadeEm2022 = datetime.date(2022, 1, 1).year - anoNascimento
        
        print("nome completo")
        
    except valueError:
        print("Ano inválido!")