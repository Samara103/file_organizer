def largest(nums):
    '''
    Return the largest number in a list

    Parameters:
        nums (list): list of numbers
    Returns:
        max (int or float): largest number from given list
    '''
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    return max


def filter_even(nums):
    '''
    Return a new list with only even numbers

    Parameters:
        nums (list): list of numbers
    Returns:
        evenNums (list): list of even numbers
    '''
    evenNums = []
    for num in nums:
        if num%2 == 0:
            evenNums.append(num)
    #return [num if num%2 == 0 else None for num in nums]
    return evenNums


def count_occurrences(nums, value):
    '''
    Count how many times a value appears

    Parameters:
        nums (list): list of numbers
        value (int or float): value to count number of appearances
    Returns:

    '''
    count = 0 
    for num in nums:
        if num == value:
            count += 1
    #return nums.count(value)
    return count


def reverse_list(nums):
    '''
    Reverse a list (without using list.reverse())

    Parameters:
        nums (list): list of numbers
    Returns:
        newList (list): list of numbers in reverse order
    '''
    newList = []
    for index in range(len(nums)-1, -1, -1):
        newList.append(nums[index])
    #return nums[::-1]
    return newList


def is_sorted(nums):
    '''
    Check if a list is sorted

    Parameters:
        nums (list): list of numbers
    Returns:
        sorted (boolean): whether given list is sorted
    '''
    curr = nums[0]
    for num in nums[1:]:
        if num < curr:
            return False
        curr=num
    return True

print(largest([1,5,3]))
print(filter_even([1,2,3,4]))
print(count_occurrences([1,1,2,3,1],1))
print(reverse_list([1,2,3]))
print(is_sorted([1,2,3]))
print(is_sorted([3,1,2]))