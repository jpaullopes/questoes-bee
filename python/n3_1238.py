#função que recebe as duas palavras em uma linha e retorna eas separadas 
def words_separator(word,word_number):
    for c in word:
        if c == ' ':
            if word_number == 1:
                return str(word[0:word.index(c)])
            else:
                return str(word[word.index(c) + 1:])


#função que vai cominar as duas palavras em uma
def words_combinator(word_1,word_2):
    new_word = ''

    if len(word_1) < len(word_2):
        little_word = len(word_1)
        biggest_word = word_2
    else:
        little_word = len(word_2)
        biggest_word = word_1


    for c in range(little_word):
        new_word += (word_1[c] + word_2[c])

    new_word +=  biggest_word[little_word:]
    return new_word


def main():
    
    count_words = int(input())

    for w in range(count_words):
        inp = str(input())
        first_word = words_separator(inp,1)
        second_word = words_separator(inp,2)

        combined_words = words_combinator(first_word,second_word)

        print(combined_words)


main()