def ComputarMaiorValor(Valor_1,Valor_2):
    if(Valor_2 > Valor_1):
        return Valor_2
    return Valor_1


def ComputarMenorValor(Valor_1,Valor_2):
    if(Valor_2 < Valor_1):
        return Valor_2
    return Valor_1


def main():
    Valor_1 = int(input())
    Valor_2 = int(input())

    Menor_Valor = ComputarMenorValor(Valor_1,Valor_2)
    Maior_Valor = ComputarMaiorValor(Valor_1,Valor_2)

    Contador = Menor_Valor
    Soma_Multiplos = 0

    while (Contador <= Maior_Valor):
        
        if not(Contador % 13 == 0):
            Soma_Multiplos += Contador

        Contador += 1

    print(Soma_Multiplos)


main()