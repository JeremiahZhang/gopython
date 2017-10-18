def search(x, nums):
    if x in nums:
        return nums.index(x)
    else:
        return -1

def linear_search(x, nums):
    for i in len(nums):
        if nums[i] == x:
            return i
        else:
            reutrn -1

def binary_search(x, nums):
    nums.sort()
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        item = nums[mid]

        if x == item:
            return mid
        elif x < item:
            high = mid - 1
        else:
            low = mid + 1

    return -1

def main():
    x1 = 2
    x2 = 7
    nums = [3, 4, 2, 1, 5]

    # y1 = search(x1, nums)
    y1 = binary_search(x1, nums)
    y2 = search(x2, nums)
    print(y1)
    print(y2)

if __name__ == '__main__':
    main()
