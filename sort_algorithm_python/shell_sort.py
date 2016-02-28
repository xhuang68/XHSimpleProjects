__author__ = 'xiaohuang'


def shell_sort(array):
    n = len(array)
    gap = n/2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j>=gap and array[j-gap] > temp:
                array[j] = array[j-gap]
                j = j - gap
            array[j] = temp
        gap = gap / 2
    return array

array = [5, 7, 3, 4, 6, 9, 8, 1, 0, 2]
result = shell_sort(array)
print result