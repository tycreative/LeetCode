def twoSum(nums: [int], target: int) -> [int]:
    numbers = {} # initialize dict for storing numbers

    for i in range(len(nums)): # iterate through numbers array
        remaining = target - nums[i] # subtract current number from target
        if remaining in numbers.keys(): # check if calc value in numbers dict
            return [i, numbers[remaining]] # return indexes
        numbers[nums[i]] = i # otherwise add current number to dict

assert twoSum([2,7,11,15], 9) == [1, 0]
assert twoSum([3,2,4], 6) == [2, 1]
assert twoSum([3,3], 6) == [1, 0]
