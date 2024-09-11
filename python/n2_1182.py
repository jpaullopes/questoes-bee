def my_reduce(func,array,initial_value):
    #acomulador
    accomulator = initial_value 
    #iteração
    for i in array:
        #acomular cada valor
        accomulator = func(accomulator,i)
    #retorna
    return accomulator

#função que vai pegar os elemento das coluna selecionada pelo user
def get_column(choiced_column, array):
    column_array = []
    for i in range(len(array)):
        column_array.append(array[i][choiced_column])
    
    return column_array


def array_operation(choice_operation,choice_column,array):
    #pegar a coluna escolhida
    column = get_column(choice_column,array)
    #selecionar o tipo de operação
    #usar o reduce
    if choice_operation == 'S':
        return my_reduce(lambda a,b: a + b,column,0)
    #média
    return my_reduce(lambda a,b:a + b,column,0) / len(array)
    #retornar resultado



def main():
    read_column = int(input())#receber a coluna que vai ser lida
    type_of_operation = input()#receber o tipo de operação que vai ser executada

    matriz = []
    #vai receber os valores
    for i in range(12):
        line = []
        for j in range(12):
            line.append(float(input()))
        matriz.append(line)

    #calcular tudo
    final_result = array_operation(type_of_operation,read_column,matriz)
    #exibir resultado
    print(round(final_result,1))


main()