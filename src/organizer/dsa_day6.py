def is_palindrome(pal):
    '''
    Check if string is a palindrome (ignore spaces and case)

    Parameters:
        pal (str): string to check
    Returns 
        bool: if given string is a palindrome or not
    '''
    pal = pal.lower().replace(" ",'') #get rid of spaces and change everything to lower case
    i=0
    j=len(pal)-1
    while i<=j:
        if pal[i] != pal[j]:
            return False
        i+=1
        j-=1
    return True


def first_unique_char(line):
    '''
    Return the first non-repeating character

    Parameters:
        line (str): string of characters
    Returns:
        str: first non-repeating character
        None: if there are no non-repeating characters in given string
    '''
    letters = {}
    for a in line:
        if a not in letters:
            letters[a] = 1
        else:
            letters[a] +=1
    for letter in letters:
        if letters[letter] == 1:
            return letter
    return None


def is_anagram(str1, str2):
    '''
    Check if two strings are anagrams (same letters, just rearranged)

    Parameters:
        str1 (str): first word
        str2 (str): second word
    Returns
        bool: if the words are anagrams of each other
    '''
    if len(str1) != len(str2): #make sure both words are the same length
        return False
    freq = {}
    for a in str1:
        freq[a] = freq.get(a,0)+1
    for a in str2:
        if a not in freq:
            return False
        freq[a] -=1
        if freq[a]<0:
            return False
    return True


def longest_unique_substring(line):
    '''
    Return the longest substring without repeating characters

    Parameters:
        line (str): string to count substrings
    Returns:
        int: count of longest substring
    '''
    seen = set()
    left = 0
    maxLen = 0
    for right in range(len(line)):
        while line[right] in seen:
            seen.remove(line[left])
            left +=1
        seen.add(line[right])
        maxLen = max(maxLen, right-left+1)
    return maxLen
    '''maxCount = 0
    i=0
    j=0
    substring = []
    while i<len(line)-1:
        while line[i] in substring:
            del substring[0]
            j+=1
        substring.append(line[i])
        maxCount = max(maxCount, i-j+1)
        i+=1
    return maxCount'''


def contains(str1, str2):
    '''
    Return true if string B is a substring of string A

    Parameters:
        str1 (str): string A
        str2 (str): string B
    Returns
        bool: if string B is a substring of string A
    '''
    if len(str1)< len(str2):
        return False
    window = len(str2)
    i=0
    j=window-1
    while j<len(str1):
        if str1[i:j+1]==str2:
            return True
        i+=1
        j+=1
    return False
    '''could use just i to compute window slice...
    window = len(str2)
    for i in range(len(str1) - window +1):
        if str1[i:i+window] == str2:
        return True
    return False
    '''


#print(is_palindrome("Race car")) #true
#print(first_unique_char("swiss")) #w
#print(is_anagram("listen", "silent")) #true
#print(longest_unique_substring("abcabcbb")) #3
#print(contains("hello world", "world")) #true