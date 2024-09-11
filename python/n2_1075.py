def main():

    Valor_N = int(input())

    Contador = 0
    while Contador < 10000:
        Contador += 1

        if (Contador % Valor_N == 2):
            print(Contador)

main()