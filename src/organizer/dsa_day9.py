def most_frequent_char(line):
    '''
    Return the most frequent character in a string 

    Parameters:
        line (str): string to count characters
    Returns:
        char: most frequent character
    '''
    letters = {}
    maxCount = 0
    maxChar = None
    for ch in line:
        if ch not in letters:
            letters[ch] = 1
        else:
            letters[ch] +=1
    for letter in letters:
        if letters[letter] > maxCount:
            maxCount = letters[letter]
            maxChar = letter
    return maxChar


def isomorphic(str1, str2):
    '''
    Check if two strings are isomorphic

    Parameters:
        str1 (str): string 1
        str2 (str): string 2
    Returns:
        Boolean: true of the 2 strings are isomorphic
    '''
    if len(str1)!=len(str2):
        return False
    map1={}
    map2={}
    for c1, c2 in zip(str1, str2):
        if c1 in map1 and map1[c1]!=c2:
            return False
        if c2 in map2 and map2[c2]!=c1:
            return False
        map1[c1]=c2
        map2[c2]=c1
    return True
    '''old... wrong!
    if len(str1) != len(str2) or len(set(str1))!=len(set(str2)): #if lengths or number of unique chars not the same
        return False
    index =0
    while index<len(str1)-2:
        curr1 = str1[index]
        curr2 = str2[index]
        while str1[index+1]==curr1 and str2[index+1]==curr2:
            index+=1
        if str1[index+1]==curr1 and str2[index+1]!=curr2:
            return False
        if str1[index+1]!=curr1 and str2[index+1]==curr2:
            return False
        index+=1
    return True'''


def group_anagrams(strs):
    '''
    Group words that are anagrams

    Parameters:
        strs (list): list of strings
    Returns:
        list: list of lists with anagrams grouped
    '''
    words = {}
    for word in strs:
        letters = {}
        for let in word:
            if let in letters:
                letters[let] +=1
            else:
                letters[let]=1
        found = False
        for wrd in words:
            if words[wrd][0] == letters:
                words[wrd][1].append(word)
                found = True
        if not found:
            words[word] = [letters, [word]]
    out = []
    for word in words:
        out.append(words[word][1])
    return out
    '''another way...
    groups = {}
    for word in strs:
        key = ''.join(sorted(word))             #if sort word, collapse into the same key (all same letters grouped together in alphabetical ordwr)
        groups.setdefault(key,[]).append(word)  #if key in dict, use existing list, if not create new list
    return list(groups.values())                #get all the vales from the keys
    '''

def first_repeat(str1):
    '''
    DReturn the first repeated character

    Parameters:
        str1 (str): string to count characters
    Returns:
        str: first repeated character
    '''
    letters = {}
    for ch in str1:
        if ch in letters:
            return ch
        else:
            letters[ch]=1
    return None

def count_freq(list1):
    '''
    Count how many times each number appears

    Parameters:
        list1 (list): list of numbers to count frequency
    Returns:
        dict: dictionary with number found as key and value the frequency count
    '''
    nums = {}
    for num in list1:
        if num in nums:
            nums[num]+=1
        else:
            nums[num]=1
    return nums

#print(most_frequent_char("banana")) #a
#print(isomorphic("egg", "add")) #true
#print(isomorphic("foo", "bar")) #false
#print(group_anagrams(["eat","tea","ate","bat"])) #→ [["eat","tea","ate"], ["bat"]]
#print(first_repeat("swiss")) #s
print(count_freq([1,2,2,3,3,3])) #→ {1:1, 2:2, 3:3}

