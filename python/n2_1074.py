def EvenOrOdd(Number):

    if Number % 2 == 0:
        return 'EVEN'
    
    return 'ODD'

def PositiveorNegative(Number):

    if Number > 0:
        return 'POSITIVE'
    
    return 'NEGATIVE'

def main():
    Quantidade_Iterações = int(input())
    Contador = 0

    while Contador < Quantidade_Iterações:

        Contador += 1
        Numero_Informado = int(input())

        if Numero_Informado == 0:

            TypeNumber = 'NULL'
        else:
            EverOdd = EvenOrOdd(Numero_Informado)
            PosiOrNeg = PositiveorNegative(Numero_Informado)

            TypeNumber = f'{EverOdd} {PosiOrNeg}'

        print(TypeNumber) 
               
main()