import time



trocos = [70, 20, 60, 68, 85, 104, 217, 99, 201, 369]
# moedas = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
moedas = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

for x in trocos:
    inicio = time.time()
    trocoRestante = x
    moedasGastas = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # moedasGastas = 0
    i = len(moedas)-1

    print("\nPara o troco de: " + str(trocoRestante) + " é necessário:")
    qtdMoedas = 0
    while trocoRestante > 0:
        if (trocoRestante - moedas[i]) >= 0:
            trocoRestante -= moedas[i]
            moedasGastas[i]+=1
            qtdMoedas += 1
        else:
            if qtdMoedas > 0:
                print(str(qtdMoedas) + " moeda(s) de " + str(moedas[i]))
                qtdMoedas = 0
            i -= 1
    print(str(qtdMoedas) + " moeda(s) de " + str(moedas[i]))
    fim = time.time()
    print("Tempo gasto -> " + str(fim - inicio) +"\n")