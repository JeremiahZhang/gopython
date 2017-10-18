def select_sort(nums):
    n = len(nums)

    # For each positon in the list
    for bottom in range(n-1):
        # bottom is smallest initially
        mp = bottom
        for i in range(bottom+1, n):
            if nums[i] < nums[mp]:
                mp = i

        # swap smallest item to the bottem
        nums[bottem], nums[mp] = nums[mp], nums[bottom]
