# -*- coding: utf-8 -*-

# Quick sort
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    # 中间数
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

if __name__ == '__main__':
    arr = [3, 6, 8, 10, 0, 1, 2]
    results = quicksort(arr)
    print results
