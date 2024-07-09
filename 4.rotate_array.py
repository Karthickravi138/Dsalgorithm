def rotate_array(nums, k):
    n = len(nums)
    k = k % n  
    if k == 0:
        return nums
    nums.reverse()
    nums[:k] = reversed(nums[:k]) 
    nums[k:] = reversed(nums[k:])
    return nums