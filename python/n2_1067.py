def main():
    
    NumeroDeEntrada = int(input())
    NumeroImpar = int()

    while NumeroImpar < NumeroDeEntrada:
        NumeroImpar += 1

        if NumeroImpar % 2 > 0:
            print(NumeroImpar)


main()