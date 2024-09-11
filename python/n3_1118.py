def ValidaçãoDeNota():
    Nota = float(input())

    while not(0 <= Nota <= 10):
        print('nota invalida')
        Nota = float(input())

    return Nota

def PedirResposta():

    Resposta = int(input())

    while (Resposta != 1 and Resposta != 2):
        print('novo calculo (1-sim 2-nao)')
        Resposta = int(input())

    return Resposta


def main():

    Resposta = 1
    while Resposta != 2:

        Nota_1 = ValidaçãoDeNota()
        Nota_2 = ValidaçãoDeNota()
        Media_Notas = (Nota_1 + Nota_2) / 2

        print(f'media = {Media_Notas:.2f}')

        print('novo calculo (1-sim 2-nao)')
        Resposta = PedirResposta()

main()