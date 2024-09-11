#vai adicionar mais 3 ao núemero correspondente na tabela ASCII e retornar qual é o novo caracter no texto, caso seja uma letra
def PrimeiroPasso(Texto):
    NovoTexto = ''

    for c in Texto:
        if (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122):
            LetraModificada = ord(c) + 3
            NovoTexto += chr(LetraModificada)
        else:
            NovoTexto += c

    return NovoTexto


#função que vai inverter o texto
def SegundoPasso(Texto):
    NovoTexto = ''

    for c in Texto:
        NovoTexto = c + NovoTexto

    return NovoTexto


#função que vai pegar a segunda metada truncada do texto e vai diminuir menos 1 nos caracters e retornar eles segundo a tabela ASCII
def TerceiroPasso(Texto):

    NovaMetade = ''

    #trunca as metades
    MetadePrimaria = Texto[0:int(len(Texto) / 2)]
    MetadeSecundaria = Texto[int(len(Texto) / 2):]

    for c in MetadeSecundaria:

        LetraModificada = ord(c) - 1 
        NovaMetade += chr(LetraModificada)

    NovoTexto = MetadePrimaria + NovaMetade

    return NovoTexto


#função que realiza a criptografia do texto
def Criptografia(Texto):

    MensagemSemiCriptografada = PrimeiroPasso(Texto)
    MensagemSemiCriptografada = SegundoPasso(MensagemSemiCriptografada)
    MensagemCriptografada = TerceiroPasso(MensagemSemiCriptografada)

    return MensagemCriptografada


def main():
    #entrada de dados
    Count = int(input())#"informe a quantidade de mensagens criptografadas: "

    for m in range(Count):
        Mensagem = input()#"informe a mensagem a ser criptografada: "

        MensagemCriptografada = Criptografia(Mensagem)

        print(MensagemCriptografada)


main()