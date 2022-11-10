import time
inicio = time.time()


def buscaProx(distPercorrida, posicao):
    cidadeAtual =matrizDistancias[posicao]
    menorDistancia = 999999
    cidComMenorDistancia = 0
    cidDisponivel = 1
    for i in range(len(cidadeAtual)):
        if (cidadeAtual[i] != 0 and visitados[i] != 1):
            if (menorDistancia > cidadeAtual[i]):
                menorDistancia = cidadeAtual[i]
                cidComMenorDistancia = i
                cidDisponivel = 0
    if (cidDisponivel == 1):
        distPercorrida = distPercorrida + matrizDistancias[0][posicao]
        return distPercorrida
    else:
        visitados[cidComMenorDistancia] = 1
        distPercorrida = distPercorrida + menorDistancia
        return buscaProx(distPercorrida, cidComMenorDistancia)


n = 20  # número de cidades
visitados = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
matrizDistancias = [
    [0, 10, 15, 20, 40, 40, 10, 17, 29, 50, 29, 74, 12, 25, 27, 50, 21, 33, 12, 10],
    [10, 0, 35, 25, 20, 52, 42, 12, 55, 6, 44, 77, 33, 3, 23, 54, 12, 12, 11, 1],
    [15, 35, 0, 30, 30, 11, 99, 45, 2, 33, 21, 65, 23, 55, 12, 52, 66, 12, 23, 13],
    [20, 25, 30, 0, 15, 22, 42, 12, 54, 6, 12, 43, 65, 10, 22, 9, 75, 12, 22, 32],
    [40, 20, 30, 15, 0, 32, 3, 12, 55, 34, 45, 12, 56, 31, 53, 65, 12, 43, 42, 12],
    [40, 52, 11, 22, 32, 0, 66, 32, 21, 54, 65, 91, 44, 23, 11, 82, 71, 43, 54, 23],
    [10, 42, 99, 42, 3, 66, 0, 76, 11, 56, 2, 64, 3, 54, 6, 1, 21, 43, 45, 54],
    [17, 12, 45, 12, 12, 32, 76, 0, 34, 65, 54, 76, 98, 32, 12, 54, 76, 72, 12, 12],
    [29, 55, 2, 54, 55, 21, 11, 34, 0, 23, 43, 3, 33, 4, 12, 33, 3, 2, 43, 43],
    [50, 6, 33, 6, 34, 54, 56, 65, 23, 0, 54, 33, 21, 23, 12, 34, 11, 45, 55, 87],
    [29, 44, 21, 12, 45, 65, 2, 54, 43, 54, 0, 12, 11, 23, 54, 6, 98, 2, 32, 43],
    [74, 77, 65, 43, 12, 91, 64, 76, 3, 33, 12, 0, 4, 32, 12, 54, 65, 76, 44, 76],
    [12, 33, 23, 65, 56, 44, 3, 98, 33, 21, 11, 4, 0, 3, 23, 21, 43, 54, 6, 1],
    [25, 3, 55, 10, 31, 23, 54, 32, 4, 23, 23, 32, 3, 0, 12, 32, 12, 3, 56, 22],
    [27, 23, 12, 22, 53, 11, 6, 12, 12, 12, 54, 12, 23, 12, 0, 43, 5, 4, 65, 5],
    [50, 54, 52, 9, 65, 82, 1, 54, 33, 34, 6, 54, 21, 32, 43, 0, 44, 5, 55, 65],
    [21, 12, 66, 75, 12, 71, 21, 76, 3, 11, 98, 65, 43, 12, 5, 44, 0, 66, 77, 5],
    [33, 12, 12, 12, 43, 43, 43, 72, 2, 45, 2, 76, 54, 3, 4, 5, 66, 0, 4, 45],
    [12, 11, 23, 22, 42, 54, 45, 12, 43, 55, 32, 44, 6, 56, 65, 55, 77, 4, 0, 5],
    [10, 1, 13, 32, 12, 23, 54, 12, 43, 87, 43, 76, 1, 22, 5, 65, 5, 45, 5, 0]

]
visitados[0] = 1
distPercorrida = 0

distanciaFinal = buscaProx(distPercorrida, 0)


print(f"A distância percorrida é de: {distanciaFinal}")

fim = time.time()
print(f"Tempo gasto: {fim - inicio}")