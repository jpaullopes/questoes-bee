def ComputarMaiorValor(Valor_1,Valor_2):
    if(Valor_2 > Valor_1):
        return Valor_2
    return Valor_1


def ComputarMenorValor(Valor_1,Valor_2):
    if(Valor_2 < Valor_1):
        return Valor_2
    return Valor_1


def main():

    NumeroDeIteracoes = int(input())
    ContadorIteracoes = 0

    while ContadorIteracoes < NumeroDeIteracoes:
        ContadorIteracoes += 1

        ValoresRecebidos = input().split()
        Valor_X = int(ValoresRecebidos[0])
        Valor_Y = int(ValoresRecebidos[1])

        Menor_Valor = ComputarMenorValor(Valor_X,Valor_Y)
        Maior_Valor = ComputarMaiorValor(Valor_X,Valor_Y)

        Contador = Menor_Valor + 1
        SomaDeValores = 0

        while (Contador < Maior_Valor):
            
            if (Contador % 2 > 0):
                SomaDeValores += Contador

            Contador += 1

        print(SomaDeValores)

main()