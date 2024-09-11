def main():
    NumeroDeLinhas = int(input())
    Contador = 0
    Valor_1 = 1

    while Contador < NumeroDeLinhas:
        Contador += 1
        Valor_2 = Valor_1 + 1
        Valor_3 = Valor_1 + 2
        print(f'{Valor_1} {Valor_2} {Valor_3} PUM')
        Valor_1 += 4


main()