def main():
    while True:
        try:
            tamanho = input()
            matriz_formatada = matriz123(criador_matriz(int(tamanho),3))
            print(exibir_matriz(matriz_formatada))
        except EOFError:
            break    


def matriz123(matriz):
    nova_matriz = matriz[:]
    for i in range(len(nova_matriz)):
        nova_matriz[i][i] = 1
        nova_matriz[i][-(i + 1)] = 2
    return nova_matriz


#cria uma matriz com tamnha n cheia de 0
def criador_matriz(tamanho,elemento):
    matriz = []
    for i in range(tamanho):
        line = []
        for j in range(tamanho):
            line.append(elemento)
        matriz.append(line)
    return matriz

def exibir_matriz(lista):
    matriz = ''
    for i in range(len(lista) - 1):
        for c in (my_map(str,lista[i])):
            matriz += c
        matriz += f'\n'
    for c in (my_map(str,lista[len(lista) - 1])):
        matriz += c
        
    return matriz


def my_map(func,lista):
    nova_lista = []
    for i in lista:
        nova_lista.append(func(i))
    return nova_lista


main()