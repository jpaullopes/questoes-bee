#função responsavel por contar o número total de leds em um número 
def count_leds(numbers):
    leds_list = [6,2,5,5,4,5,6,3,7,6]
    sum_leds = 0

    for c in str(numbers):
        sum_leds += leds_list[int(c)]

    return sum_leds


def main():
    tests = int(input())

    #pra cada iteração o número é informado e o número total de leds é fornecido
    for t in range(tests):
        number = int(input())

        leds_number = count_leds(number)

        print(leds_number , 'leds')


main()