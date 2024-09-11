def ComputarMaiorValor(Valor_1,Valor_2):
    if(Valor_2 > Valor_1):
        return Valor_2
    return Valor_1


def ComputarMenorValor(Valor_1,Valor_2):
    if(Valor_2 < Valor_1):
        return Valor_2
    return Valor_1


def main():
    Valor_X = int(input())
    Valor_Y = int(input())

    Menor_Valor = ComputarMenorValor(Valor_X,Valor_Y)
    Maior_Valor = ComputarMaiorValor(Valor_X,Valor_Y)

    Contador = Menor_Valor + 1

    while (Contador < Maior_Valor):
        
        if (Contador % 5 == 2 or Contador % 5 == 3):
            print(Contador)

        Contador += 1



main()