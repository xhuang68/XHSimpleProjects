__author__ = 'xiaohuang'


def insertion_sort(array):
    length = len(array)
    for i in range(1, length):
        insertValue = array[i]
        while i > 0 and array[i-1] > insertValue:
            array[i] = array[i-1]
            i -= 1
        array[i] = insertValue
    return array

array = [5, 7, 3, 4, 6, 9, 8, 1, 0, 2]
result = insertion_sort(array)
print result