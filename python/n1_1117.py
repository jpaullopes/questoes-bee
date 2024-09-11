def ValidaçãoDeNota():
    Nota = float(input())

    while not(0 <= Nota <= 10):
        print('nota invalida')
        Nota = float(input())

    return Nota

def main():

    Nota_1 = ValidaçãoDeNota()
    Nota_2 = ValidaçãoDeNota()
    Media_Notas = (Nota_1 + Nota_2) / 2

    print(f'media = {Media_Notas}')

main()