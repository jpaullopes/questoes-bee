#função responsavel por corrigir os valores
def values_corrector(failed_digit, wrong_number):
    new_number = '0'

    for c in wrong_number:
        if c != failed_digit:
            new_number += c

    return int(new_number)


def main():
    #entrada dos dados
    inp = str(input())
    failed_digit = inp[:1]
    number = inp[2:]

    while failed_digit != '0' and number != '0':

        correct_number = values_corrector(failed_digit, number)
        print(correct_number)

        inp = str(input())
        failed_digit = inp[:1]
        number = inp[2:]


main()