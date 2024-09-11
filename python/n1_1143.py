def main():
    
    ValorDeEntrada = int(input())
    Contador = 0
    
    while Contador < ValorDeEntrada:
        Contador += 1
        Numero_Quadrado = Contador ** 2
        Numero_Cubo = Contador ** 3
        print(f'{Contador} {Numero_Quadrado} {Numero_Cubo}')
        
    
main()