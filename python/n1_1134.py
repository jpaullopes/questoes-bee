def ValidarPedido():
    Pedido = int(input())

    while not(1 <= Pedido <= 4):
        Pedido = int(input())

    return Pedido 


def main():

    TipoDeCombustivel = ValidarPedido()
    Alcool = Gasolina = Disel = 0

    while TipoDeCombustivel != 4:

        if(TipoDeCombustivel == 1):
            Alcool += 1
        elif(TipoDeCombustivel == 2):
            Gasolina += 1
        elif(TipoDeCombustivel == 3):
            Disel += 1

        TipoDeCombustivel = ValidarPedido()
    
    print(f"""MUITO OBRIGADO
Alcool: {Alcool}
Gasolina: {Gasolina}
Diesel: {Disel}""")


main()