#vai pegar as primeiras letras de cada palavra para formar a mensagem
def discover_hidden_menssage(words):
    secret_word = ''
    menssage = words.split()

    for c in menssage:
        secret_word += c[0]

    return secret_word


def main():
    #entrada de dados
    count = int(input(''))

    for t in range(count):
        #entrada de dados
        word = input('')

        secret_menssage = discover_hidden_menssage(word)

        print(secret_menssage)


main()