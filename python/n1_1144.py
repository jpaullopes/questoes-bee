def main():

    ValorDeEntrada = int(input())
    Contador = Valor_1 = 0

    while Contador < (ValorDeEntrada * 2):
        Contador += 2
        Valor_1 += 1

        Valor_2 = Valor_1 ** 2
        Valor_3 = Valor_1 ** 3
        print(f'{Valor_1} {Valor_2} {Valor_3}')
        print(f'{Valor_1} {Valor_2 + 1} {Valor_3 + 1}')
       
                 
main()