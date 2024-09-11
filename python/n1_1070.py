def main():
    
    NumeroDeEntrada = int(input())
    NumeroImpar = NumeroDeEntrada
    Contador = 0

    while Contador < 6:

        if NumeroImpar % 2 > 0:
            Contador += 1
            print(NumeroImpar)
            
        NumeroImpar += 1


main()