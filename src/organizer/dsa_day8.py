def balanced(nums):
    '''
    Check if parenthesis is balanced

    Parameters:
        nums (str): string of parenthesis
    Returns:
        Boolean: if given string has balanced parenthesis 
    '''
    #push only opening brackets
    #when see closing bracket
        #if stack is empty, unbalanced
        #else pop top and check if matches
    #at end stack should be empty
    stack = []
    pairs = {')':'(', ']':'[', '}':'{'}
    for c in nums:
        if c in '([{':
            stack.append(c)
        else:
            if not stack:
                return False
            if stack.pop() != pairs[c]:
                return False
    return len(stack)==0
    '''stack = []
    for c in nums:
        stack.append(c)
    while len(stack)>0:
        x = stack.pop()
        y = stack.pop()
        if not y=='(' and x==')' or not y=='[' and x==']' or not y=='{' and x=='}':
            return False
    return True'''
    
def remove_duplicates(nums):
    '''
    Remove duplicates from a list using a set

    Parameters:
        nums (list): list of numbers
    Returns
        list: list of non-repeating/ duplicate numbers
    '''
    final = set()
    for num in nums:
        final.add(num)
    return list(final)


def all_unique(nums):
    '''
    return true if a string has all unique characters

    Parameters:
        nums (str): string to count characters
    Returns:
        Boolean: true if there are no repeating characters
    '''
    unique = set(nums)
    if len(unique)==len(nums):
        return True
    return False


def process_tasks(tasks):
    '''
    Use queue to simulate processing tasks

    Parameters:
        tasks (list): list of tasks
    Returns:
        list: list of tasks in the order they were processed
    '''
    queue = []
    start=0
    end=0
    for task in tasks:
        queue.append(task)
        end +=1
    finalList = []
    while start!=end:
        finalList.append(queue[start])
        start+=1
    return finalList
    ''' another way...
    from collections import deque
    def process_tasks(tasks):
        queue = deque(tasks)
        result = []
        while queue:
            result.append(queue.popleft())
        return result
    '''


def reverse_string(line):
    '''
    use a stack to reverse the string

    Parameters:
        line (string): string to reverse
    Returns:
        Str: reversed string 
    '''
    stack = []
    for ch in line:
        stack.append(ch)
    finalString = ''
    while len(stack)>0:
        finalString+=stack.pop()
    return finalString

#print(balanced("()()"))
#print(balanced("(]"))
#print(remove_duplicates([1,2,2,3,1])) #[1,2,3]
#print(all_unique("abcde")) # → True
#print(all_unique("hello"))  # → False
#print(process_tasks(["a","b","c"])) #→ ["a","b","c"]
#print(reverse_string("hello")) #→ "olleh"