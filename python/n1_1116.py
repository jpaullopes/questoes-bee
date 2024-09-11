def main():

    Quantidade_Iteraçoes = int(input())
    Contador = 0

    while Contador < Quantidade_Iteraçoes:
        Contador += 1

        ValoresInformados = input().split()
        Valor_X = int(ValoresInformados[0])
        Valor_Y = int(ValoresInformados[1])

        if(Valor_Y == 0):
            print('divisao impossivel')
        else:
            Divisao = Valor_X / Valor_Y
            print(f'{Divisao:.1f}')

main()