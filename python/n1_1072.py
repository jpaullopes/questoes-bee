def VerificarDentroIntervalo(Valor):
    if ( 10 <= Valor <= 20):
        return True
    return False

def main():

    NumeroDeRepeticoes = int(input())
    Contador = 0
    QuantidadeIn = QuantidadeOut = 0

    while Contador < NumeroDeRepeticoes:

        Contador += 1
        ValorVerificado = int(input())
        
        if(VerificarDentroIntervalo(ValorVerificado)):
            QuantidadeIn += 1
        else:
            QuantidadeOut += 1 
        
    print(f'{QuantidadeIn} in')
    print(f'{QuantidadeOut} out')

main()