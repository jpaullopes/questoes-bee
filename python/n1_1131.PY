def DefinirResultado(Inter,Gremio):

    if Inter > Gremio:
        return 'Inter venceu mais'
    elif Gremio > Inter:
        return 'Gremio venceu mais'
    else:
        return 'Nao houve vencedor'


def main():
    Resposta = 1
    QuantidadeGrenais = 0
    VitoriasInter = VitoriasGremio = Empates = 0
    NumeroDeGols = ''

    while Resposta != 2:
        QuantidadeGrenais += 1

        NumeroDeGols = input().split()
        GolsInter = int(NumeroDeGols[0])
        GolsGremio = int(NumeroDeGols[1])

        if(GolsInter > GolsGremio):
            VitoriasInter += 1
        elif(GolsGremio > GolsInter):
            VitoriasGremio += 1
        else:
            Empates += 1

        print('Novo grenal (1-sim 2-nao)')
        Resposta = int(input())

    Resultado = DefinirResultado(VitoriasInter,VitoriasGremio)

    Tabela = f"""{QuantidadeGrenais} grenais
Inter:{VitoriasInter}
Gremio:{VitoriasGremio}
Empates:{Empates}
{Resultado}"""
    
    print(Tabela)


main()