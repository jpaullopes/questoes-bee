def my_filter(func,array):
    new_array = []
    for i in array:
        if func(i):
            new_array.append(i)
    return new_array


#algoritmo de sortemaento de listas
def insertion_sort(array):
    array_copy = array[:]  # Cria uma cópia do array original para preservar o original
    for i in range(1, len(array_copy)):
        key = array_copy[i]
        j = i - 1
        while j >= 0 and array_copy[j] > key:
            array_copy[j + 1] = array_copy[j]
            j -= 1
        array_copy[j + 1] = key
    return array_copy


#o problema de apresentação de erro 100% está aqui
#formata para a apresentação
def formatation(array):
    formated = ""
    for j in array:
        formated += f"{j[0]}:{j[-1]}, "  # Formata pares de letras consecutivas
    formated = f"{formated[:-2]}"  # Remove a vírgula e espaço finais
    return formated


#função principal que retorna a faixa de letras
def lyrics_track_processor(text):
    array = my_filter(lambda a: a != ' ',text)  # Remove espaços em branco da string
    array = insertion_sort(array)  # Ordena a lista de caracteres

    letter_list = []
    sub_list = [array[0]]
    first_letter = array[0]

    for j in range(1, len(array)):
        if ord(array[j]) - 1 == ord(first_letter) or ord(array[j]) == ord(first_letter):
            sub_list.append(array[j])  # Adiciona a letra à sublista se for consecutiva
        else:
            letter_list.append(sub_list[:])  # Armazena a sublista de letras consecutivas
            sub_list = []
            sub_list.append(array[j])
        first_letter = array[j]
    
    if sub_list:
        letter_list.append(sub_list)  # Adiciona a última sublista, se existir
    
    return letter_list


def main():
    while True:
        try:
            text = input('')
            if not text.strip():  # Verifica se a entrada está vazia ou contém apenas espaços
                print(" ")
                continue
            
            letters_strip = lyrics_track_processor(text)
            print(formatation(letters_strip))  # Exibe a formatação final das sequências de letras
        except EOFError:
            break


main()
