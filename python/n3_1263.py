def aliteration(text):

    text_list = text.split()
    count = 0
    is_sequence = False

    for i in range(len(text_list) - 1):

        if text_list[i][0] == text_list[i + 1][0]:
            if not is_sequence:
                count += 1
                is_sequence = True

        else:
            is_sequence = False
    
    return count

def main():
    try:
        while True:

            text = input().lower()
            count_aliteration = aliteration(text)
            print(count_aliteration)
            
    except EOFError:
        pass

main()
