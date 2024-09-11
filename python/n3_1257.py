#pedi ao chatgpt pra comentar 

def hash_calculator(array):
    alfabetic = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']   

    sum = 0
    for indx, element in enumerate(array):  # Índice do elemento na lista
        for ind, letter in enumerate(element):  # Índice da letra na string
            sum += indx + ind + alfabetic.index(letter)  # Cálculo da soma dos índices
    
    return sum


def main():
    
    tests = int(input())  # Número de testes a serem executados

    for t in range(tests):
        lines_array = []

        lines = int(input())  # Número de linhas para o teste atual
        for c in range(lines):
            lines_array.append(input())
        
        hash = hash_calculator(lines_array)

        print(hash)  # Imprime o valor do hash


main()
