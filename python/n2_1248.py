def my_join(array):
    new_word = ''

    for c in array:
        new_word += c

    return new_word


def insertion_sort(array):
    array_copy = array[:]

    for i in range(1,len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        
        array[j + 1] = key
    
    return array_copy
    

def diet_verificator(diet, consumidos):
    dinner = ''
    diet_copy = insertion_sort(diet)
    consumidos_copy = insertion_sort(consumidos)
    teco = []

    diet_count = diet_copy.count()


    for c in consumidos_copy:
        if c not in diet_copy:
            return 'CHEATER'
    
    
    for d in diet_copy:
        if d not in consumidos_copy:
            dinner += d

    


def main():
    diet = 'EDSMB'
    consu = 'MSDS'

    print(diet_verificator(diet,consu))


main()