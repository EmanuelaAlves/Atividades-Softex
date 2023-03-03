#variáveis
candidato_x = 0
candidato_y = 0
candidato_z = 0
votos_brancos = 0
votos_nulos = 0
votos_totais = 0

while True:
    voto = input("Digite o número do candidato (1 para X, 2 para Y, 3 para Z) ou 0 para voto em branco: ")
    
    if voto == "fim":
        break
        
    try:
        voto = int(voto)
        
        if voto == 0:
            votos_brancos += 1
            votos_totais += 1
            print("Voto em branco registrado com sucesso.")
        elif voto == 1:
            candidato_x += 1
            votos_totais += 1
            print("Voto para o candidato X registrado com sucesso.")
        elif voto == 2:
            candidato_y += 1
            votos_totais += 1
            print("Voto para o candidato Y registrado com sucesso.")
        elif voto == 3:
            candidato_z += 1
            votos_totais += 1
            print("Voto para o candidato Z registrado com sucesso.")
        else:
            votos_nulos += 1
            votos_totais += 1
            print("Voto nulo registrado com sucesso.")
            
    except ValueError:
        print("Erro: Digite apenas números ou 'fim' para finalizar a votação.")

print("Votação encerrada.\n")
print("Candidato X: ", candidato_x, " votos.")
print("Candidato Y: ", candidato_y, " votos.")
print("Candidato Z: ", candidato_z, " votos.")
print("Votos em branco: ", votos_brancos)
print("Votos nulos: ", votos_nulos)
print("Total de votos: ", votos_totais)

if candidato_x > candidato_y and candidato_x > candidato_z:
    print("\nO candidato X venceu a eleição!")
elif candidato_y > candidato_x and candidato_y > candidato_z:
    print("\nO candidato Y venceu a eleição!")
elif candidato_z > candidato_x and candidato_z > candidato_y:
    print("\nO candidato Z venceu a eleição!")
else:
    print("\nA eleição terminou empatada!")