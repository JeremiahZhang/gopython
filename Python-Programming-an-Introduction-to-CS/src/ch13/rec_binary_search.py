def rec_bin_search(x, nums, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    item = nums[mid]
    if item == x:
        return mid
    elif x < item:
        return rec_bin_search(x, nums, low, mid-1)
    else:
        return rec_bin_search(x, nums, mid+1, high)

def search(x, nums):
    return rec_bin_search(x, nums, 0, len(nums)-1)

def main():
    x = 3
    nums = [0, 1, 2, 3, 4, 6, 8]
    result = search(x, nums)
    print(result)

if __name__ == '__main__':
    main()
