
def NumeroMenor(Valor_1,Valor_2):
    MenorNumero = Valor_1
    if Valor_2 < Valor_1:
        MenorNumero = Valor_2
    return MenorNumero


def NumeroMaior(Valor_1,Valor_2):
    MaiorNumero = Valor_1
    if Valor_2 > Valor_1:
        MaiorNumero = Valor_2
    return MaiorNumero


def main():

    NumeroRecebidos = input().split()
    Valor_M = int(NumeroRecebidos[0])
    Valor_N = int(NumeroRecebidos[1])

    while (Valor_N > 0 and Valor_M > 0):

        Menor_Valor = NumeroMenor(Valor_M, Valor_N)
        Maior_Valor = NumeroMaior(Valor_M, Valor_N)

        Soma_Valores = 0
        Numero_Acrescido = Menor_Valor
        while not(Numero_Acrescido > Maior_Valor):

            Soma_Valores += Numero_Acrescido
            print(Numero_Acrescido,end=' ')
            Numero_Acrescido += 1

        print(f'Sum={Soma_Valores}')
        Menor_Valor = 0

        NumeroRecebidos = input().split()
        Valor_M = int(NumeroRecebidos[0])
        Valor_N = int(NumeroRecebidos[1])


main()