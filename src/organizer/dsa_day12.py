def longest_consecutive(nums: list[int]) ->int:
    '''
    Given unsorted array of ints, return length of longest sequence of consecutive integers (in any order)
    The sequence does not need to be continuous in the array
    
    :param nums: list of integers (may contain duplicates)
    :type nums: list[int]
    :return: Integer representing length of longest consecutive sequence
    :rtype: int
    '''
    #num is start of set of num-1 is not in set, then expand forward num, num+1, num+2...
    numSet = set(nums)
    longest = 0
    for num in numSet:
        if num-1 not in numSet:
            length = 1
            curr = num
            while curr+1 in numSet:
                curr+=1
                length+=1
            longest = max(longest, length)
    return longest
    '''sortedNums = sorted(nums)
    print(sortedNums)
    longest = -1
    right = 0
    count = 1
    for left in range(1,len(nums)):
        print(sortedNums[right],sortedNums[left])
        if sortedNums[right]+1!=sortedNums[left]:
            right = left
            count = 1
        else:
            count+=1
            longest = max(longest, count)
            right+=1
    return longest'''


def top_k_frequent(nums: list[int], k:int)->list[int]:
    '''
    given integer array nums and an integer k, return k most frequent elements
    return result in any order
    
    :param nums: list of integers
    :type nums: list[int]
    :param k: Dnumber of most frequent elements to return
    :type k: int
    :return: a list of k integers represneting the most frequent elements
    :rtype: list[int]
    '''
    #frequency map
    freq = {}
    for n in nums:
        freq[n] = freq.get(n,0)+1
    
    #buckets: index = frequency
    buckets = [[] for _ in range(len(nums)+1)]
    for num, count in freq.items():
        buckets[count].append(num)
    
    #collect from highest freq down
    output = []
    for count in range(len(buckets)-1, 0, -1):
        for num in buckets[count]:
            output.append(num)
            if len(output)==k:
                return output
    return output
    '''sortedNums = sorted(nums)
    print(sortedNums)

    freq = {}
    start = 0
    end = 0
    while end<len(sortedNums):
        while sortedNums[end] == sortedNums[start] and end+1<len(sortedNums):
            end+=1
        if end-start in freq:
            freq[end-start].append(sortedNums[start])
        else:# end-start not in freq:
            freq[end-start] = [sortedNums[start]]
        start = end
        end+=1
    print(freq)
    output = []
    while len(output)<k and len(freq):
        curr = freq.pop(max(freq.keys()))
        for item in curr:
            output.append(item)
    return output'''


def is_anagram(s: str, t:str) ->bool:
    '''
    given two strings s and t, return true if t is an anagram of s, and false otherwise
    
    :param s: first string
    :type s: str
    :param t: second string
    :type t: str
    :return: indicate whether string are anagrams
    :rtype: bool
    '''
    if not len(s) == len(t):
        return False
    freqS = {}
    freqT = {}
    for i in range(len(s)):
        freqS[s[i]] = freqS.get(s[i],0)+1
        freqT[t[i]] = freqT.get(t[i],0)+1
    return freqT==freqS


#print(longest_consecutive([100,4,200,1,3,2])) #4 ... [1,2,3,4]
#print("output:",top_k_frequent([1,1,1,2,2,3,4,4,4],2)) #[1,2]
#print(is_anagram('anagram', 'nagaram'))
