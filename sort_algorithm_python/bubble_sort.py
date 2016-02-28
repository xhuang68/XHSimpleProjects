__author__ = 'xiaohuang'


def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(1, length-i):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array


array = [5, 7, 3, 4, 6, 9, 8, 1, 0, 2]
result = bubble_sort(array)
print result