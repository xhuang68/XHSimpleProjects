__author__ = 'xiaohuang'

def insertion_sort(nums):
    for i in range(len(nums)):
        s_idx = i
        s = nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] < s:
                s_idx = j
                s = nums[j]
        temp = nums[i]
        nums[i] = nums[s_idx]
        nums[s_idx] = temp
    return nums

array = [5, 7, 3, 4, 6, 9, 8, 1, 0, 2]
result = insertion_sort(array)
print result
