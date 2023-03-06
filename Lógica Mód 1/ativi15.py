def bubble_sort(l):
    trocou = True
    while trocou:
        trocou = False
        for i in range(len(l)):
            if i + 1 < len(l):
                if l[i] > l[i+1]:
                    l[i], l[i+1] = l[i+1], l[i]
                    trocou = True

    return l

lista = [5, 2, 0, 7, 1]
nova_lista = bubble_sort(lista)
print(nova_lista)