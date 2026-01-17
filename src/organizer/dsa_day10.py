def is_palindrome(nums):
    '''
    Two pointers: check if list is a palindrome
    
    Parameters:
        nums (list): list of integers
    Returns:
        Boolean: true if list is a palindrome
    '''
    index = 0
    while index<len(nums)//2:
        if not nums[index]== nums[len(nums)-1-index]:
            return False
        index+=1
    return True


def two_sum_sorted(nums, k):
    '''
    Two Pointers: find two numbers that sum to target (sorted list)

    Parameters:
        nums (list): list of numbers
        k (int): target sum
    Returns:
        tuple: 2 indicies of elements that sum to target
    '''
    start =0
    end = len(nums)-1
    while start<end:
        sum = nums[start] + nums[end]
        if sum==k:
            return (start, end)
        elif sum>k:
            end-=1
        else:
            start+=1
    return None


def max_window_sum(nums,k):
    '''
    Fixed Window: max sum of any window of size k

    Parameters:
        nums (list): list of integers
        k (int): window size
    Returns: 
        int: max sum based on window size
    '''
    start = 0
    end = k
    maxSum =-1
    while end<len(nums)+1:
        sum = 0
        for i in nums[start:end]:
            sum += i
        print(nums[start:end], sum)
        maxSum = max(maxSum, sum)
        start+=1
        end+=1
    return maxSum
    #better way... keep running sum and add new element entering, subtract element leaving window


def longest_unique(line):
    '''
    Dynamic Window: length of longest substring without repeating characters

    Parameters:
        line (str): string
    Returns:
        int: length of longest substring found without repeating characterrs
    '''
    seen = set()
    start = 0
    maxLen = 0
    for end in range(len(line)):
        while line[end] in seen:
            seen.remove(line[start])
            start+=1
        seen.add(line[end])
        maxLen = max(maxLen, end-start+1)
    return maxLen
    '''
    start =0
    end =2
    maxCount = -1
    while end<len(line)+1:
        substring = line[start:end]
        letters = set(substring)
        if len(substring)==len(letters):
            maxCount = max(maxCount, len(substring))
            end+=1
        else:
            start+=1
    return maxCount'''


def min_subarray_len(nums, k):
    '''
    Dynamic Window: smallest subarray with sum>= target

    Parameters:
        nums (list): list of numbers
        k (int): target sum
    Returns:
        int: length of smallest subarray with sum>= target
    '''
    start =0
    currSum = 0
    minLen = float('inf')
    for end in range(len(nums)):
        currSum += nums[end]
        while currSum >=k:
            minLen = min(minLen, end-start+1)
            currSum-=nums[start]
            start+=1
    return minLen if minLen!=float('inf') else 0
    '''
    minSub = float('inf')
    start = 0
    end = 1
    while end<len(nums)+1:
        checkSum = sum(nums[start:end])
        if checkSum >= k:
            minSub = min(minSub, len(nums[start:end]))
            start+=1
        else:
            end+=1
    return minSub'''
#print(is_palindrome([1,2,3,2,1])) #true
#print(two_sum_sorted([1,2,4,6,10], 8)) #true
#print(max_window_sum([1,2,3,4,5], 2)) #9
#print(longest_unique("abcabcbb")) #3
#print(min_subarray_len([2,3,1,2,4,3], 7)) #2