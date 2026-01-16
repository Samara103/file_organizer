'''def greet(name):
    return f"Hello {name}, welcome to Day 1!"

print(greet())'''
import os
#if os.path.exists("x.txt")

#from organizer.utils import checkIfEven
#from organizer.file_practice import readAndPrintFile
#from organizer.file_practice import writeToFile
#from organizer.file_practice import countLinesInFile
#from organizer.dsa_day3 import reverse_list
from organizer.dsa_day5 import same_elements
from organizer.dsa_day5 import prefix_sum
from organizer.dsa_day7 import factorial


def main():
    #print(checkIfEven(11))
    #readAndPrintFile("testText.txt")
    #writeToFile(['start', 'middle', 'end'], "C:/Users/Samara/Documents/GitHub/testText.txt")
    #readAndPrintFile("C:/Users/Samara/Documents/GitHub/testText.txt")
    #print(countLinesInFile("C:/Users/Samara/Documents/GitHub/testText.txt"))
    #print(countLinesInFile("testText.txt"))
    #print(reverse_list([1,2,4]))
    #print(first_unique([4,5,1,2,1,4,5])) #2
    #print(same_elements([1,2,3], [3,2,1])) #true
    #print(prefix_sum([1,2,3,4]))
    print(factorial(6))

if __name__ == '__main__':
    main()

