def insertion_sort(array):
    array_copy = array[:]

    for i in range(1,len(array_copy)):
        key = array_copy[i]
        j = i - 1

        while j >= 0 and array_copy[j] > key:
            array_copy[j + 1] = array_copy[j]
            j = j -1
        
        array_copy[j + 1] = key
    
    return array_copy


def my_filter(func,array):
    new_array = []

    for i in array:
        if func(i):
            new_array.append(i)
    return new_array


def main():
    word_1 = 'Hey This java is hot'.lower()
    word_2 = 'Java is a new paradigm'.lower()



main()