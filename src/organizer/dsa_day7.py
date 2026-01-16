def linear_search(nums, target):
    '''
    linear search. return index of target or -1

    Parameters:
        nums (list): list of numbers, sorted in ascending order
        target (int or float): target number
    Returns:
        int: index of found target or -1 if target was not found
    '''
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


def binary_search(nums, target):
    '''
    Binary search. return index of target or -1

    Parameters:
        nums (list): list of numbers, sorted in ascending order
        target (int or float): target number to find index
    Returns:
        int: index of target or -1 if not found
    '''
    start = 0
    end = len(nums)-1
    while start<=end:
        mid = (start+end)//2
        if nums[mid]==target:   #found the target, so return index
            return mid
        if nums[mid]<target:    #target bigger than curr so use second half of list
            start = mid+1
        else:                   #target smaller than curr so use first half of list
            end = mid-1
    return -1


def count_smaller(nums, target):
    '''
    Count how many numbers are smaller than the target

    Parameters:
        nums (list): list of numbers
        target (int or float): target largest number
    Returns:
        int: count of numbers smaller than target, or 0 if none
    '''
    nums = sorted(nums)
    index = binary_search(nums, target)
    if index != -1:
        return index
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)


def factorial(num):
    '''
    Recursion, compute the factorial

    Parameters:
        num (int): number to compute factorial
    Returns:
        int: factorial of num
    '''
    if num<=1:
        return 1
    return num*factorial(num-1)
    

def sum_digits(num):
    return sum_digits_recursive(str(abs(num)))

def sum_digits_recursive(nums):
    if len(nums)==1:
        return int(nums)
    return int(nums[0])+sum_digits_recursive(nums[1:])


#print(linear_search([1,3,5,7], 5)) #2
#print(binary_search([1,3,5,7], 7)) #3
#print(count_smaller([3,1,4,2], 3)) #3
#print(factorial(5)) #120
#print(sum_digits(1234)) #10