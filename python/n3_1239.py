#função que vai converter certos digitos para o padrão html
def text_converssor_html(text):
    new_text = ''
    count_intalic = 0
    count_bolder = 0
    for c in text:
        if c == '_':
            if count_intalic == 0:
                new_text += '<i>'
                count_intalic += 1
            else:
                new_text += '</i>'
                count_intalic = 0
        elif c == '*':
            if count_bolder == 0:
                new_text += '<b>'
                count_bolder += 1
            else:
                new_text += '</b>'
                count_bolder = 0
        else:
            new_text += c

    return new_text


def main():
    try:
        while True:
            text = input('')
            html_text = text_converssor_html(text)

            print(html_text)

    except EOFError:
        pass


main()