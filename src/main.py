'''def greet(name):
    return f"Hello {name}, welcome to Day 1!"

print(greet())'''
import os
#if os.path.exists("x.txt")

from organizer.utils import checkIfEven
from organizer.file_practice import readAndPrintFile
from organizer.file_practice import writeToFile
from organizer.file_practice import countLinesInFile

#print(checkIfEven(11))
#readAndPrintFile("testText.txt")
#writeToFile(['start', 'middle', 'end'], "C:/Users/Samara/Documents/GitHub/testText.txt")
#readAndPrintFile("C:/Users/Samara/Documents/GitHub/testText.txt")
#print(countLinesInFile("C:/Users/Samara/Documents/GitHub/testText.txt"))
print(countLinesInFile("testText.txt"))

