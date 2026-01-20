#multi-pattern problems

def longest_k_distinct(s, k):
    '''
    Longest substring with at most k distinct characters.
    Patterns: dynamic sliding window + frequency map

    Parameters:
        s (str): string
        k (int): upper bound for distinct characters
    Returns:
        int: length of substring with at most k distinct characters
    '''
    start = 0
    freq = {}
    longest = 0
    for end in range(len(s)):
        freq[s[end]] = freq.get(s[end], 0)+1 #add new character
        while len(freq)>k: #shrink window until valid
            freq[s[start]] -=1
            if freq[s[start]]==0:
                freq.pop(s[start])
            start+=1
        longest = max(longest, end-start+1)
    return longest
    '''start =0
    end = 0
    charFreq = {}
    longest = 0
    while end<len(str1):
        newChar = str1[end]
        if newChar in charFreq: #repeated character
            charFreq[newChar] += 1
            print(newChar,'is already in charFreq so +1: ', charFreq)
        elif newChar not in charFreq and len(charFreq)+1<=k: #new character but less than cap
            charFreq[newChar] = 1
            print(charFreq)
        else: #new character and at cap
            charFreq[newChar] = 1
            while len(charFreq)>k:
                if charFreq.get(str1[start])>1:
                    charFreq[str1[start]]-=1
                else:
                    a=charFreq.pop(str1[start])
                    print(str1[start],'removed')
                start+=1
        longest = max(longest, sum(charFreq.values()))
        end+=1
    print(charFreq)
    return longest'''


def two_sum_unsorted(nums, k):
    '''
    Find all pairs that sum to a target (unsorted list)
    Patterns: two pointers and hash map

    Parameters:
        nums (list): unsorted list of ints
        k (int): target sum 
    Returns:
        list: list of tuple pairs that sum to target
    '''
    pairs = []
    for i in range(len(nums)):
        pairs.append((nums[i],i))
    pairs.sort()

    left = 0
    right = len(nums)-1
    output = []
    while left<right:
        sum = pairs[left][0] + pairs[right][0]
        if sum==k:
            output.append((pairs[left][1], pairs[right][1]))
            left+=1
            right-=1
        elif sum<k:
            left+=1
        else:
            right-=1
    return output


def valid_wildcard(s):
    '''
    Validate a string of braclets with wildcard '*'
    Patterns: stack and range tracking
    '*' can act as '(' ')' or empty

    Parameters:
        str1 (str):
    Returns:
        boolean: if brackets balanced
    '''
    #use range tracking, not stack
    low = 0
    high = 0
    for ch in s:
        if ch=='(':
            low +=1
            high+=1
        elif ch==')':
            low-=1
            high-=1
        else: # '*'
            low-=1
            high+=1
        
        if high<0:
            return False
        if low<0:
            low=0
    return low==0
'''    stack = []
    index = 0
    for i in range(len(s)):
        if s[i] in ('(', '['):
            stack.append(s[i])
            index+=1
        elif s[i]=='*':
            if i<len(s)//2: #append to stack
                stack.append(s[i])
                index+=1
            else: #burn something in stack with a wild card
                a = stack[index-1]
                index-=1
        elif s[i] in (')', ']'):
            if len(stack)==0:
                return False
            a = stack[index-1]
            index-=1
            if a!='(' and s[i]==')' and a!='*':
                return False
            if a=='*' and len(stack)>0:
                b = stack[index-1]
                if b in ('(', '*'):
                    index-=1
    return True'''


def longest_mountain(nums):
    '''
    Return the length of the longest mountain in the array
    Patterns: two pointers and scanning
    - a mountain is: strictly up, then strictly down

    Parameters:
        nums (list): list of numbers
    Returns:
        int: length of longest mountain
    '''
    n = len(nums)
    longest = 0
    i=1
    while i<n-1:
        if nums[i-1]<nums[i]<nums[i+1]: #check if nums[i] is peak
            left = i-1
            right = i+1
            while left>0 and nums[left-1]<nums[left]: #expand left (uphill)
                left-=1
            while right<n-1 and nums[right]>nums[right+1]: #expand right (downhill)
                right +=1
            longest = max(longest, right-left+1)
            i = right
        else:
            i+=1
    return longest
    '''start = 0
    end = 0
    longest = 0
    while end<len(nums)-1:
        count = 0
        while nums[start]<nums[end]:
            count+=1
            end+=1
        while nums[start]>nums[end]:
            count+=1
            end+=1
        longest = max(longest, end-start+1)
        start=end
        end+=1
    return longest'''


def group_people(people):
    '''
    Group people by their group size
    Patterns: hash map, list building

    Parameters:
        nums (list): list of integers, each index is person ID, each value is group size that person belongs to
    Returns:
        list: list of person IDs (indexes) where people share group size specified
    '''
    groups = {}
    output = []
    for id, size in enumerate(people):
        if size not in groups:
            groups[size] = []
        groups[size].append(id)
        if len(groups[size])==size:
            output.append(groups[size])
            groups[size] = []
    return output
    '''freq = {}
    for i in range(len(people)):
        if people[i] in freq:
            freq[people[i]].append(i)
        else:
            freq[people[i]] = [i]
    output = []
    group = []
    while len(freq)>0:
        size = max(freq)
        a = freq[size].pop(0)
        group.append(a)
        if len(group)==size:
            output.append(group)
            group = []
        if len(freq[size])<=0:
            freq.pop(size)
    return output'''
#print(longest_k_distinct("eceba", 2)) #3
#print(two_sum_unsorted([3,1,5,7,5,9], 10)) #→ [(0,3), (2,4)]
#print(valid_wildcard("(*)"))# → True
#print(valid_wildcard("(*))"))# → True
#print(longest_mountain([2,1,4,7,3,2,5]))# → 5
print(group_people([3,3,3,3,3,1,3])) #→ [[0,1,2], [3,4,6], [5]]

