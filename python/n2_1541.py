def main():
    while True:
        medidas =  input().split()
        if medidas[0] == '0':
            break
        A, B, C = my_map(int,medidas)
        tamanho_terreno = computar_area(A,B,C)
        print(tamanho_terreno)


def computar_area(medida_a,medida_b,porcentagem):
    area = ((medida_a * medida_b) * 100)/ porcentagem
    medida_lado = int(area ** 0.5)

    return medida_lado


def my_map(func,lista):
    nova_lista = []
    for i in lista:
        nova_lista.append(func(i))
    return nova_lista


main()