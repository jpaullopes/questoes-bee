def count_pag(max_line_page,max_character_line,text):
    count_character = count_words = count_lines = 0
    count_pag = 0
    characters = 0

    list_words = text.spit()

    for word in list_words:
        characters += len(word) + 1

        if characters == max_character_line:
            count_lines += 1
            characters = 0
    

def main():
    text = 'Se mana Piedade tem casado com Quincas Borba apenas me daria uma esperanca colateral'

    total_pag = count_pag(4,20,text)

    print(total_pag)


main()