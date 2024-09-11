def is_letter(character):
    return (ord(character) >= 65 and ord(character) <= 90) or (ord(character) >=97 and ord(character) <= 122)


def my_upper(letter):
    if ord(letter) >= 65 and ord(letter) <= 90:
        return letter
    return chr(ord(letter) - 32)
    

def my_lower(letter):
    if ord(letter) >= 97 and ord(letter) <= 122:
        return letter
    return chr(ord(letter) + 32)


def dancing_sentence(text):
    new_text = ''
    count = 0
    for c in text:
        if is_letter(c):

            if count % 2 == 0:
                new_text += my_upper(c)
            else:
                new_text += my_lower(c)

            count += 1

        else:
            new_text += c

    return new_text


def main():

    try:
        while True:
            text = input()

            text_dancing_sentence = dancing_sentence(text)

            print(text_dancing_sentence)
    
    except EOFError:
        pass


main()