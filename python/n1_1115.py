def DeterminadorQuadrante(CoordenadaX, CoordenadaY):
    if(CoordenadaX > 0):

        if(CoordenadaY > 0):
            return 'primeiro'
        
        else:
            return 'quarto'

    else:
        if(CoordenadaY > 0):

            return 'segundo'
        else:
            return 'terceiro'


def main():

    ValoresDeEntrada = input().split()
    Valor_CooredenaX = int(ValoresDeEntrada[0])
    Valor_CooredenaY = int(ValoresDeEntrada[1])

    while (Valor_CooredenaY != 0 and Valor_CooredenaX != 0):

        coordenada = DeterminadorQuadrante(Valor_CooredenaX , Valor_CooredenaY)
        print(coordenada)

        ValoresDeEntrada = input().split()
        Valor_CooredenaX = int(ValoresDeEntrada[0])
        Valor_CooredenaY = int(ValoresDeEntrada[1])


main()