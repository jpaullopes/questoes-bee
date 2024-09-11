def main():

    Valor_I = 1
    while Valor_I < 10:
        Valor_J = 7
        Contador = 0
        while Contador < 3:

            print(f'I={Valor_I} J={Valor_J}')
            Contador += 1
            Valor_J -= 1

        Valor_I += 2

main()