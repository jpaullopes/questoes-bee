def DefinirOrdem(ValorX,ValorY):
    if(ValorX < ValorY):
        return 'Crescente'
    return 'Decrescente'

def main():

    ValoresDeEntrada = input().split()
    Valor_X = int(ValoresDeEntrada[0])
    Valor_Y = int(ValoresDeEntrada[1])

    while (Valor_X != Valor_Y):

        Ordem = DefinirOrdem(Valor_X,Valor_Y)
        print(Ordem)

        ValoresDeEntrada = input().split()
        Valor_X = int(ValoresDeEntrada[0])
        Valor_Y = int(ValoresDeEntrada[1])


main()