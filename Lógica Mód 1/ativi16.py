def insertion_sort(vetor):
    n = len(vetor)
    for i in range(1, n):
        valor_atual = vetor[i]
        j = i - 1
        while j >= 0 and vetor[j] > valor_atual:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = valor_atual
    return vetor

# Inicialização do vetor com números ímpares em ordem não-crescente
vetor = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]
print("Vetor antes da ordenação:", vetor)
vetor_ordenado = insertion_sort(vetor)
print("Vetor ordenado:", vetor_ordenado)