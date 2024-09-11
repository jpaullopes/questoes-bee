#sinceramente eu achei bem feio isso aqui
#vai retornar o número de cilcos que a máquina vai precisar fazer para a sequencia de passos infomada
def number_cycles(sequence_tracks,max_process):
    count_process = 0
    count = 0

    for x in sequence_tracks:
        if x == 'R':
            count_process += 1

            if count_process == max_process:
                count += 1
                count_process = 0

        elif x == 'W':

            if count_process > 0:
                 count += 1
                 count_process = 0

            count += 1
    #se sobrar algum processo de R
    if count_process > 0:
        count += 1

    return count
        

#o problema inteiro da questão era esse negocio de while e EOF...(nem sei tratamento de erro ainda)
def main():

    while True:

        try:
            #entrada de dados
            corrent_sequence = input()
            corrent_max_process = int(input())

            cycles = number_cycles(corrent_sequence,corrent_max_process)

            #saída
            print(cycles)

        except EOFError:
            break



main()