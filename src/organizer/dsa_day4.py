def second_largest(nums):
    '''
    find the second largest number.

    Parameter:
        nums (list): list of numbers
    '''
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num and num > second:
            second = num
    return second


def has_duplicates(nums):
    '''
    return true if list has a duplicates.

    Parameters:
        nums (list): list of numners
    '''
    items = set() #doesn't allow diplicates
    for num in nums:
        if num in items:
            return True
        items.add(num)
    return False


def pair_sums(nums):
    '''
    return the sum of every pair of adjacent numbers.

    Parameters:
        nums (list): list of numbers
    '''
    pairs = []
    for i in range(len(nums)-1):
        pairs.append(nums[i] + nums[i+1])
    return pairs


def longest_increasing(nums):
    '''
    find the longest increating sequence.

    Parameters: 
        nums (list): list of numbers
    '''
    maxCount = 1
    count = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            count += 1
        else:
            maxCount = max(maxCount, count)
            count = 1
    '''first, second = 0,1
    maxCount =  0
    count = 0
    while second<len(nums):
        if nums[first]+1==nums[second]:
            count +=1
        else:
            maxCount = max(count, maxCount)
            count = 0
        second +=1
        first +=1'''
    return max(maxCount, count)


def max_window_sum(nums,k):
    '''
    sliding window: max sum of any window of size k

    Parameters:
        nums (list): list of numbers
    '''
    first = 0
    maxCount = 0
    while first+k<=len(nums): #for start in range(len(nums)-k+1):
        windowSum=0
        for i in range(first,first+k): #range(start, start+k)
            windowSum+= nums[i]
        maxCount = max(maxCount, windowSum)
        first+=1
    return maxCount

#print(second_largest([1, 5, 3, 4]))
#print(has_duplicates([1,2,3,1]))
#print(pair_sums([1,2,3]))
#print(longest_increasing([1,2,2,3,4,5]))
#print(max_window_sum([1,2,3,4,5], 2))



