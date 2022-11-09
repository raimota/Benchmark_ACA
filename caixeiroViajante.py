import time
import os
inicio = time.time()


def buscaProx(distPercorrida, posicao):
    cidadeAtual = matrizDistancias[posicao]
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


n = 5  # número de cidades
visitados = [0, 0, 0, 0, 0]
matrizDistancias = [
    [0, 10, 15, 20, 40],
    [10, 0, 35, 25, 20],
    [15, 35, 0, 30, 30],
    [20, 25, 30, 0, 15],
    [40, 20, 30, 15, 0]

]
visitados[0] = 1
distPercorrida = 0

distanciaFinal = buscaProx(distPercorrida, 0)

fim = time.time()
print(f"A distância percorrida é de: {distanciaFinal}")
print(f"Tempo gasto: {fim - inicio}, inicio={inicio},fim={fim}")
os.system("pause")
