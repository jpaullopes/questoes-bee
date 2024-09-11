#adiciona os espaços entre as palavras
def add_spaces(word_list):
    new_word = ''
    for x in range(len(word_list) - 1):
        new_word += word_list[x] + ' '

    new_word += word_list[-1]

    return new_word


#percorre todos os elementos dessa lista e encontra o valor da palavra com maior tamanho
def count_length_biggest_word(word_array):
    biggest_word = len(word_array[0])
    for w in word_array:
        if biggest_word < len(w):
            biggest_word = len(w)
    
    return biggest_word


#ALINHA TODAS AS PALAVRAS PARA A ESQUERDA DE ACORDO COM O TAMANHO
def my_rjust(word,length):
    new_word = word
    while len(new_word) < length:
        new_word = ' ' + new_word
    
    return new_word


def main():
    count = 0
    while True:

        tests = int(input(''))

        if tests == 0:
            break

        if count > 0:
            print('')

        phrases_list = []
        for c in range(tests):
            words = input('').split()
            phrases_list.append(add_spaces(words))
        
        length_biggest_phrase = count_length_biggest_word(phrases_list)

        for p in phrases_list:
            temp_word = my_rjust(p,length_biggest_phrase)
            print(temp_word)

        count += 1


main()