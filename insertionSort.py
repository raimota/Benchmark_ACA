import time
inicio = time.time()


def insertionSort(vet):
    j = 0
    for i in range(1, len(vet)):
        x = vet[i]
        j = i
        while(j > 0 and x < vet[j-1]):
            vet[j] = vet[j-1]
            j -= 1
        vet[j] = x


vet = [2, 1, 10, 8, 5, 7, 3, -1]
insertionSort(vet)
print(vet)
vet.append(-5)
print(vet)
insertionSort(vet)
print(vet)
fim = time.time()
print(f"Tempo execução: {fim - inicio}")
