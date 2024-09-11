def main():

    Valor_J = 10
    Valor_I = 0

    while not(Valor_I > 20):
        
        Contador = 0
        while Contador < 3:
            Contador += 1

            if (Valor_I == 0 or Valor_I == 10 or Valor_I == 20):

                print(f'I={int(Valor_I / 10)} J={int(Valor_J / 10)}')
            else:

                print(f'I={Valor_I/10} J={(Valor_J/10)}') 
            Valor_J += 10 

        Valor_J -= 28         
        Valor_I += 2

main()