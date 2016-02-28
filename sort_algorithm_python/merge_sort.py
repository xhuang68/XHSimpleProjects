__author__ = 'xiaohuang'


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) / 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result


array = [5, 7, 3, 4, 6, 9, 8, 1, 0, 2]
result = merge_sort(array)
print result