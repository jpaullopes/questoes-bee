def main():

    NumeroDeEntrada = int(input())
    Contador = 0

    while not(Contador > NumeroDeEntrada):
        Contador += 1
        
        if Contador % 2 == 0:
            print(f'{Contador}^2 = {Contador ** 2}')

main()