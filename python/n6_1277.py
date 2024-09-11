#vai separar as palavras segundo o espaço que elas vão ter
def words_separator(words,position):
    words_list = words.split()

    return words_list[position]


#retorna o percentual de presença de um aluno segundo a chamada
def presence_verificator(presence):
    count = len(presence)
    presence_count = 0

    for p in presence:
        if p == 'P':
            presence_count += 1
            #se for por atestado ele vai desconsiderar e subtrair do todo
        elif p == 'M':
            count -= 1
    
    return presence_count / count * 100


def main():
    tests = int(input())

    for t in range(tests):
        missing_names = ''

        #ENTRADA DE DADOS
        number_names = int(input())
        names = str(input())
        presence = str(input())
        
        for n in range(number_names):
            
            corrent_name = words_separator(names,n)
            corrent_presence = words_separator(presence,n)

            presence_percentage = presence_verificator(corrent_presence)

            if presence_percentage < 75:
                missing_names += (f'{corrent_name} ')
            
        print(missing_names[:-1])
            

main()