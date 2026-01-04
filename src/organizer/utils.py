def square(num):
    """
    Return the square of a number.

    Parameters:
        num (int or float): the number to square
    
        Returns:
            int or float: the squared value
    """
    return num**2

def checkIfEven(num):
    """
    Checks if a number is even.

    Parameters:
        num (int or float): the number to check if even

    Returns:
        Boolean: if num is even
    """
    return num%2 == 0

def countVowels(text):
    """
    Counts number of vowels in a string.

    Parameters:
        text (str): text to count vowels from

    Returns:
        int: number of vowels included in the provided string
    """
    #text=text.lower()
    #count=0
    #count+= text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u') + text.count('y')
    vowels = 'aeiouy'
    return sum(text.lower().count(v) for v in vowels)

def print1to20():
    """
    Loop that prints 1 to 20.

    Parameters: none
    Returns: none
    """
    for i in range(1,20+1):
        print(i)

def checkIfLegal(age):
    """
    Prints 'adult' or 'minor' based on age.

    Parameters: 
        age (int): age of person to check if legal

    Returns:
        'adult' (str): if age is greater than or equal to 18
        'minor' (str): if age is less than 18
    """
    return 'adult' if age>=18 else 'minor'

#print(countVowels('bananna'))
    