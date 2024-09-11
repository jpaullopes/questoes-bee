def TallNumber(Valor_1,Valor_2):
    Maior = Valor_1
    if Valor_2 > Valor_1:
        Maior = Valor_2
    return Maior

def main():
    Contador = 0
    Maior_Valor = 0

    while Contador < 100:
        Contador += 1
        Numero_Recebido = int(input())
        Maior_Valor = TallNumber(Maior_Valor,Numero_Recebido)

        if Maior_Valor == Numero_Recebido:
            Posicao_Numero = Contador

    print(Maior_Valor)
    print(Posicao_Numero)

main()