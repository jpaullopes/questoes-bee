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

        words_list = []
        for t in range(tests):
            word = input('')
            words_list.append(word)

        #Conta o tamanho da maior palavra na lista
        lenght_biggest_word = count_length_biggest_word(words_list)
        
        #alinhaaa
        for w in words_list:
            temp_word = my_rjust(w,lenght_biggest_word)
            print(temp_word)

        count += 1

            
main()