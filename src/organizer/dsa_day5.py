def first_unique(arr):
    '''
    Return the first non-repeating number

    Parameters:
        arr (list): list of numbers
    Returns:
        int: first non-repeating number
        None: no elements in array that are not repeating
    '''
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for num in arr:
        if freq[num] == 1:
            return num
    return None    
    '''sortedArray = sorted(arr)
    freqArr = []
    count = 1
    for i in range(1,len(arr)):
        if sortedArray[i-1] == sortedArray[i]:
            count +=1
        if sortedArray[i-1] != sortedArray[i] or i==len(arr)-1:
            freqArr.append([sortedArray[i-1], count])
            count = 1
    for item in freqArr:
        if item[1]==1:
            return item[0]
    return None'''


def same_elements(arr1, arr2):
    '''
    Return true is two lists contain the same elements (order doesn't matter)
    
    Parameters:
        arr1 (list): first list of numbers
        arr2 (list): second list of numbers
    Returns:
        bool: if two lists contain the same elements
    '''
    return sorted(arr1) == sorted(arr2)


def most_frequent(arr):
    '''
    Find the most frequent number in a list

    Parameters:
        arr (list): list of numbers
    Returns: 
        int: most frequent number in the list
    '''
    sortedArr = sorted(arr)
    freqArr = []
    count = 1
    for i in range(1,len(arr)):
        if sortedArr[i-1] == sortedArr[i]:
            count +=1
        if sortedArr[i-1] != sortedArr[i] or i==len(arr)-1:
            freqArr.append([sortedArr[i-1], count])
            count=1
    maxCount =0
    maxNum = -1
    for item in freqArr:
        if item[1] > maxCount:
            maxCount = item[1]
            maxNum = item[0]
    return maxNum
'''optional cleaner version:
    freq = {}
    for n in arr:
        freq[n] = freq.get(n, 0) + 1
    return max(freq, key=freq.get)
'''


def prefix_sum(nums):
    '''
    Return a list where each element is the running total

    Parameters:
        num (list): list of numbers
    Returns:
        list: each element is the running total
    '''
    prefixArr = [nums[0]]
    for i in range(1,len(nums)):
        sum = prefixArr[i-1] + nums[i]
        prefixArr.append(sum)
    return prefixArr


def longest_subarray(nums,k):
    '''
    Return the length of the longest subarray with sum<=k

    Parameters:
        nums (list): list of numbers
        k (int): integer max 
    Returns:
        int: length of longest subarray with sum<=k
    '''
    left = 0
    curr_sum = 0
    max_len = 0
    for right in range(len(nums)): #expand window by moving right
        curr_sum += nums[right]
        while curr_sum > k:     #shrink window if it exceeds k
            curr_sum -= nums[left]
            left += 1
        max_len = max(max_len, right - left + 1) #track longest valid window
    return max_len
    '''maxSum = float('-inf')
    left = 0
    right = len(nums)-1
    while left<right:
        sum = 0
        arr = nums[left:right]
        for i in arr:
            sum+= i
        if sum <= k and maxSum<sum:
            maxSum = sum
            left+=1
        else:
            right-=1
    return maxSum'''

#print(longest_subarray([1,2,1,1,1], 3)) #3
#print(prefix_sum([1,2,3])) #[1,3,6]
#print(most_frequent([1,2,2,3,3,3])) #3
#print(same_elements([], [])) #true
#print(first_unique([4,5,1,2,1,4,5])) #2