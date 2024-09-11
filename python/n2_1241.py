#retorna a palavra de acordo com a posição do espaço em branco
def space_separator(characters,position):
    return (characters.split())[position]


def main():
    tests = int(input())

    for t in range(tests):
        numbers = input()

        sequence_one = space_separator(numbers,0)
        sequence_two = space_separator(numbers,1)

        #verifica se a sequencia de numros 2 está na primeira sequencia
        if sequence_two in sequence_one:
            print('encaixa')
        else:
            print('nao encaixa')


main()