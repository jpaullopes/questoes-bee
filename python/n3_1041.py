def DefinirQuadrante(ValorX, ValorY):#Função que retorna qual o quadrante está o valor da coodernada
    
    if (ValorX == 0 and ValorY == 0):#caso os valores sejam iguais a zero
        return 'Origem'
    elif (ValorX != 0 and ValorY == 0):
        return 'Eixo X'
    elif (ValorX == 0 and ValorY != 0):
        return 'Eixo Y'
    
    if ValorX > 0:#caso não sejam

        if ValorY > 0:
            return 'Q1'
        else:
            return 'Q4'      
    else:

        if ValorY > 0:
            return 'Q2'
        else:
            return 'Q3'
        

def main():

    #entrada dos valores dos eixos
    ValoresEixos = input().split()
    ValorEixoX = float(ValoresEixos[0]) 
    ValorEixoY = float(ValoresEixos[1]) 

    #processamento
    ResultadoQuadrante = DefinirQuadrante(ValorEixoX,ValorEixoY)

    #exibição
    print(ResultadoQuadrante)


main()