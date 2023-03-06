def bubble_sort(vetor):
    n = len(vetor)
    for i in range(n):
        troca = False
        for j in range(n - i - 1):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                troca = True
        if not troca:
            break
    return vetor

# Teste do algoritmo
vetor = [9, 2, 8, 4, 5, 7, 1, 3, 6, 0]
print("Vetor antes da ordenação:", vetor)
vetor_ordenado = bubble_sort(vetor)
print("Vetor ordenado:", vetor_ordenado)