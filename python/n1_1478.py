def main():
    while True:

        tamanho_matriz = int(input())
        if tamanho_matriz == 0:
            break
        matriz = criador_matriz(tamanho_matriz)

        print(exibir_matriz(matriz))
        print()


def criador_matriz(tamanho):
    matriz = []
    for i in range(tamanho):
        matriz.append(criador_linha(i,tamanho))
    return matriz


def my_map(func,lista):
    nova_lista = []
    for i in lista:
        nova_lista.append(func(i))
    return nova_lista



def exibir_matriz(lista):
    matriz = ''
    for i in range(len(lista) - 1):
        for c in (my_map(str,lista[i])):
            matriz += f' {c}'
        matriz += f'\n'
    for c in (my_map(str,lista[len(lista) - 1])):
        matriz += f' {c}'
        
    return matriz

#isso aqui vai criar as linhas para matriz
#sinceramente não gostei, ficou ais otimizado e creio que tinha
#como reduzir o tamnho e melhorar
def criador_linha(numero_linha_atual,size):
    linha = [numero_linha_atual + 1]
    termo_atual = numero_linha_atual + 1
    subtrair = True
    for i in range(size - 1):
        if termo_atual == 1:
            subtrair = False
        if subtrair:
            termo_atual -= 1
        elif not subtrair:
            termo_atual += 1
        linha.append(termo_atual)
    return linha


main()