def ComputarPorcentagem(Valor, Total):
    return (Valor * 100) / Total


def main():
    QuantidadeIteracoes = int(input())
    Contador = 0
    TotalCobaias = 0
    TotalCoelhos = TotalRatos = TotalSapos = 0

    while Contador < QuantidadeIteracoes:
        Contador += 1

        ValoresDeEntrada = input().split()
        NumeroDeCobaias = int(ValoresDeEntrada[0])
        TipoDeCobaia = ValoresDeEntrada[1]

        TotalCobaias += NumeroDeCobaias

        if(TipoDeCobaia == 'C'):
            TotalCoelhos += NumeroDeCobaias
        elif(TipoDeCobaia == 'R'):
            TotalRatos += NumeroDeCobaias
        else:
            TotalSapos += NumeroDeCobaias

    PorcentagemCoelhos = ComputarPorcentagem(TotalCoelhos,TotalCobaias)
    PorcentagemRatos = ComputarPorcentagem(TotalRatos,TotalCobaias)
    PorcentagemSapos = ComputarPorcentagem(TotalSapos,TotalCobaias)

    print(f"""Total: {TotalCobaias} cobaias
Total de coelhos: {TotalCoelhos}
Total de ratos: {TotalRatos}
Total de sapos: {TotalSapos}
Percentual de coelhos: {PorcentagemCoelhos:.2f} %
Percentual de ratos: {PorcentagemRatos:.2f} %
Percentual de sapos: {PorcentagemSapos:.2f} %""")

main()