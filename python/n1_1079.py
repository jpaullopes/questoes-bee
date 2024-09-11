def MediaPonderada(N1,N2,N3):

    SomaNotas = (N1 * 2) + (N2 * 3) + (N3 * 5) 
    Media = SomaNotas / 10
    return Media

def main():

    Quantidade_Notas = int(input())
    Contador = 0

    while Contador < Quantidade_Notas:
        Contador += 1

        ValoresDeEntrada = input().split()
        Nota_1 = float(ValoresDeEntrada[0])
        Nota_2 = float(ValoresDeEntrada[1])
        Nota_3 = float(ValoresDeEntrada[2])

        ValorDaMedia = MediaPonderada(Nota_1,Nota_2,Nota_3)
        print(f'{ValorDaMedia:.1f}')


main()