__author__ = 'xiaohuang'


def quick_sort(array):
    return qsort(array, 0, len(array)-1)


def qsort(array, left, right):
    if left >= right:
        return array
    lp = left
    rp = right
    key = array[left]
    while lp < rp:
        while array[lp] < key:
            lp += 1
        while array[rp] > key:
            rp -= 1
        array[lp], array[rp] = array[rp], array[lp]
    qsort(array, left, lp-1)
    qsort(array, rp+1, right)
    return array


array = [5, 7, 3, 4, 6, 9, 8, 1, 0, 2]
result = quick_sort(array)
print result