def SelecionadorPreco(Index):#função que retorna o preço segundo o codigo e a tabela de preços
    ListaPrecos = [4, 4.5, 5, 2, 1.5]
    return ListaPrecos[Index - 1]


def main():

    #Valores de entrada; numero da opção e quantidade
    ValoresEntrada = input().split()
    OpcaoEscolhida = int(ValoresEntrada[0])
    Quantidade = int(ValoresEntrada[1])

    #processamento
    PrecoOpcaoEscolhida = SelecionadorPreco(OpcaoEscolhida)
    PrecoFinal = PrecoOpcaoEscolhida * Quantidade

    #exibição
    Total = f'Total: R$ {PrecoFinal:.2f}'
    print(Total)
    

main()