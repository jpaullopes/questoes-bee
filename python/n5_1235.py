#função que corrige as palavras erradas da impressora
def word_corrector(wrong_word):
    new_word = ''

    #pega a primeira parte da palavra e inverte
    for c in wrong_word[int(len(wrong_word)/2):]:
        new_word = c + new_word
    #pega a segunda parte e inverte
    for c in wrong_word[:int(len(wrong_word)/2)]:
        new_word = c + new_word
        
    return new_word


def main():
    count = int(input())

    for t in range(count):
        word = str(input())

        correct_word = word_corrector(word)

        print(correct_word)


main()